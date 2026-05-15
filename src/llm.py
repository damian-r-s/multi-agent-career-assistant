from typing import Optional
import os
import httpx
from langchain_ollama import ChatOllama
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


# Simple wrapper that supports a local Ollama LLM or an online OpenAI-compatible endpoint.
class LLMWrapper:
    def __init__(self):
        self.default_provider = os.getenv('LLM_PROVIDER', 'ollama')
        self.default_model = os.getenv('OLLAMA_MODEL', 'qwen2.5:7b')
        self.ollama = ChatOllama(model=self.default_model, temperature=0)
        self._override_provider: Optional[str] = None
        self._override_api_key: Optional[str] = None
        self._override_ollama_model: Optional[str] = None

    def set_override(self, provider: Optional[str], api_key: Optional[str], ollama_model: Optional[str] = None):
        self._override_provider = provider
        self._override_api_key = api_key
        self._override_ollama_model = ollama_model

    def clear_override(self):
        self._override_provider = None
        self._override_api_key = None
        self._override_ollama_model = None

    def _use_provider(self) -> str:
        return self._override_provider or self.default_provider

    def _use_ollama_model(self) -> str:
        return self._override_ollama_model or self.default_model

    def invoke(self, prompt: str) -> str:
        provider = self._use_provider()
        if provider and provider.lower() in ('openai', 'open-ai'):
            api_key = self._override_api_key or os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise RuntimeError('OpenAI provider selected but no API key provided')
            try:
                return self._call_openai_chat(prompt, api_key)
            except RuntimeError as exc:
                if 'rate limit exceeded' in str(exc).lower() and self.default_provider.lower() == 'ollama':
                    print('OpenAI rate limit reached; falling back to local Ollama provider.')
                    return self._invoke_ollama(prompt)
                raise

        return self._invoke_ollama(prompt)

    def _invoke_ollama(self, prompt: str) -> str:
        model = self._use_ollama_model()
        if model != self.ollama.model:
            self.ollama = ChatOllama(model=model, temperature=0)
        response = self.ollama.invoke(prompt)
        if hasattr(response, 'content'):
            return response.content
        return str(response)

    @retry(
        retry=retry_if_exception_type(httpx.HTTPStatusError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        reraise=True
    )
    def _openai_request(self, prompt: str, api_key: str) -> httpx.Response:
        model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': model,
            'messages': [{'role': 'user', 'content': prompt}],
            'temperature': 0
        }

        resp = httpx.post(url, json=payload, headers=headers, timeout=30.0)
        resp.raise_for_status()
        return resp

    def _call_openai_chat(self, prompt: str, api_key: str) -> str:
        try:
            resp = self._openai_request(prompt, api_key)
        except httpx.HTTPStatusError as exc:
            status_code = exc.response.status_code
            if status_code == 429:
                raise RuntimeError(
                    'OpenAI rate limit exceeded (429 Too Many Requests). ' \
                    'Please retry after a short delay or use a lower request rate.'
                ) from exc
            raise RuntimeError(
                f'OpenAI request failed with status {status_code}: {exc.response.text}'
            ) from exc
        except httpx.RequestError as exc:
            raise RuntimeError(f'Network error while calling OpenAI: {exc}') from exc

        data = resp.json()
        try:
            return data['choices'][0]['message']['content']
        except Exception:
            raise RuntimeError('Unexpected response from OpenAI: %s' % (data,))


llm = LLMWrapper()

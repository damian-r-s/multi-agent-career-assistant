import os

class JobsReaderClient:
    _client = None  # private lazy-loaded singleton

    @staticmethod
    def _get_tavily_client():
        """Private: initialize Tavily client lazily."""
        if JobsReaderClient._client is None:
            api_key = os.getenv("TAVILY_API_KEY")
            if not api_key:
                raise ValueError(
                    "TAVILY_API_KEY environment variable not set. "
                    "Set it or use without job URL extraction."
                )

            try:
                from tavily import TavilyClient
            except ImportError as exc:
                raise ImportError(
                    "The 'tavily' package is required for URL extraction. "
                    "Install it with 'pip install tavily-python'."
                ) from exc

            JobsReaderClient._client = TavilyClient(api_key=api_key)

        return JobsReaderClient._client

    @staticmethod
    def load_url_content(url):
        """Load and extract content from URL using Tavily."""
        try:
            tavily_client = JobsReaderClient._get_tavily_client()
            response = tavily_client.extract(urls=url, format="text")

            results = response.get("results", [])
            if not results:
                return "No results returned"

            return results[0].get("raw_content", "No content extracted")

        except Exception as e:
            return f"Error loading URL content: {str(e)}"

    @staticmethod
    def search_and_extract(query, max_results=3):
        """Search for information and extract content from top results."""
        try:
            tavily_client = JobsReaderClient._get_tavily_client()
            search_results = tavily_client.search(query=query, max_results=max_results)

            contents = []
            for result in search_results.get("results", []):
                url = result.get("url")
                if url:
                    content = JobsReaderClient.load_url_content(url)
                    contents.append({
                        "url": url,
                        "title": result.get("title", ""),
                        "content": content
                    })

            return contents

        except Exception as e:
            return [f"Error in search and extract: {str(e)}"]

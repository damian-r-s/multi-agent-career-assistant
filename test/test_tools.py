import os
from unittest.mock import Mock, patch

from tools import file_reader, github_api, tavily_client

def test_read_file_existing(tmp_path):
    sample_file = tmp_path / "sample.txt"
    sample_file.write_text("hello world")

    assert file_reader.read_file(str(sample_file)) == "hello world"

def test_read_file_missing():
    assert file_reader.read_file("/tmp/this-file-does-not-exist.txt") is None

@patch("tools.github_api.requests.get")
def test_fetch_github_profile_success(mock_get):
    mock_response = Mock(status_code=200)
    mock_response.json.return_value = {"login": "octocat"}
    mock_get.return_value = mock_response

    result = github_api.fetch_github_profile("octocat")

    assert result == {"login": "octocat"}
    mock_get.assert_called_once_with("https://api.github.com/users/octocat")

@patch("tools.github_api.requests.get")
def test_fetch_github_profile_failure(mock_get):
    mock_response = Mock(status_code=404)
    mock_get.return_value = mock_response

    assert github_api.fetch_github_profile("doesnotexist") is None
    mock_get.assert_called_once_with("https://api.github.com/users/doesnotexist")

def test_load_url_content_success(monkeypatch):
    fake_client = Mock()
    fake_client.extract.return_value = {"content": "extracted text"}
    monkeypatch.setattr(tavily_client, "client", fake_client)

    assert tavily_client.load_url_content("https://example.com") == "extracted text"
    fake_client.extract.assert_called_once_with(url="https://example.com")

def test_load_url_content_no_content(monkeypatch):
    fake_client = Mock()
    fake_client.extract.return_value = {}
    monkeypatch.setattr(tavily_client, "client", fake_client)

    assert tavily_client.load_url_content("https://example.com") == "No content extracted"

def test_load_url_content_exception(monkeypatch):
    fake_client = Mock()
    fake_client.extract.side_effect = RuntimeError("boom")
    monkeypatch.setattr(tavily_client, "client", fake_client)

    assert tavily_client.load_url_content("https://example.com") == "Error loading URL content: boom"

def test_search_and_extract_success(monkeypatch):
    fake_client = Mock()
    fake_client.search.return_value = {
        "results": [
            {"url": "https://example.com", "title": "Example"},
            {"title": "Missing URL"},
        ]
    }
    fake_client.extract.return_value = {"content": "content text"}
    monkeypatch.setattr(tavily_client, "client", fake_client)

    result = tavily_client.search_and_extract("query", max_results=2)

    assert result == [
        {
            "url": "https://example.com",
            "title": "Example",
            "content": "content text",
        }
    ]
    fake_client.search.assert_called_once_with(query="query", max_results=2)

def test_search_and_extract_error(monkeypatch):
    fake_client = Mock()
    fake_client.search.side_effect = ValueError("search failed")
    monkeypatch.setattr(tavily_client, "client", fake_client)

    assert tavily_client.search_and_extract("query") == ["Error in search and extract: search failed"]
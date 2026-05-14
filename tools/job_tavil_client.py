import os
from tavily import TavilyClient

# Initialize Tavily client with API key
# Set TAVILY_API_KEY environment variable
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def load_url_content(url):
    """
    Load and extract content from URL using Tavily.
    """

    try:
        response = client.extract(
            urls=url,
            format="text"
        )
        results = response.get("results", [])
        if not results:
            return "No results returned"

        return results[0].get("raw_content", "No content extracted")

    except Exception as e:
        return f"Error loading URL content: {str(e)}"

def search_and_extract(query, max_results=3):
    """
    Search for information and extract content from top results.

    Args:
        query (str): Search query
        max_results (int): Maximum number of URLs to extract

    Returns:
        list: List of extracted contents from search results
    """
    try:
        # First search
        search_results = client.search(query=query, max_results=max_results)

        contents = []
        for result in search_results.get('results', []):
            url = result.get('url')
            if url:
                content = load_url_content(url)
                contents.append({
                    'url': url,
                    'title': result.get('title', ''),
                    'content': content
                })

        return contents
    except Exception as e:
        return [f"Error in search and extract: {str(e)}"]
import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    """ Scrape the content from a given URL

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        str: The scraped text content.

    Raises:
        ValueError: If the URL is not accessible or returns an error
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text,'html.parser')

        # Extract text content from the page
        paragraphs = soup.find_all('p')
        content = ' '.join(paragraph.get_text() for paragraph in paragraphs)

        if not content:
            raise ValueError("No content found on the page")
        return content
    
    except requests.RequestException as e:
        raise ValueError(f"Failed to retrive content from the URL: {e}")
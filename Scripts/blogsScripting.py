import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import logging
from urllib.parse import urljoin, urlparse

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Function to fetch a webpage
def fetch_webpage(url):
    logging.info(f"Fetching URL: {url}")
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text


def get_all_urls(domain: str) -> set[str]:
    logging.info(f"Fetching URLs from domain: {domain}")
    # Send a request to the domain
    response = requests.get(domain)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all anchor tags
    anchor_tags = soup.find_all("a")

    # Extract and resolve URLs
    urls = set()
    for tag in anchor_tags:
        href = tag.get("href")
        if href:
            # Resolve relative URLs
            full_url = urljoin(domain, href)
            # Check if the URL belongs to the same domain
            if urlparse(full_url).netloc == urlparse(domain).netloc:
                urls.add(full_url)

    return urls


# Function to parse article titles from a webpage
def parse_articles_titles(html):
    logging.info("Parsing articles...")
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("article")
    titles = [
        article.find("h2").get_text() for article in articles if article.find("h2")
    ]
    logging.info(titles)
    return titles


# Function to count keyword frequency
def count_keywords(titles):
    logging.info("Counting keywords...")
    words = {}
    for title in titles:
        title.lower()
        for word in title.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


# Function to visualize keyword frequency
def plot_keyword_frequency(keyword_counts):
    logging.info("Plotting keyword frequency...")
    logging.info(keyword_counts)
    plt.bar(keyword_counts.keys(), keyword_counts.values())
    plt.title("Keyword Frequency in Blog Article Titles")
    plt.xlabel("Keywords")
    plt.ylabel("Frequency")
    plt.show()


# Main function
def main(urls):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_webpage, url) for url in urls]
        html_pages = [future.result() for future in futures]

    all_titles = []
    for html in html_pages:
        titles = parse_articles_titles(html)
        all_titles.extend(titles)

    keyword_counts = count_keywords(all_titles)
    plot_keyword_frequency(keyword_counts)


if __name__ == "__main__":
    urls = get_all_urls("https://blog.seancoughlin.me/")

    main(urls)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to fetch a webpage
def fetch_webpage(url):
    logging.info(f"Fetching URL: {url}")
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

# Function to parse article titles from a webpage
def parse_articles(html):
    logging.info("Parsing articles...")
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('article')
    titles = [article.find('h2').get_text() for article in articles if article.find('h2')]
    logging.info(titles)
    return titles

# Function to count keyword frequency
def count_keywords(titles, keywords):
    logging.info("Counting keywords...")
    keyword_counts = {keyword: 0 for keyword in keywords}
    for title in titles:
        for keyword in keywords:
            keyword_counts[keyword] += title.lower().split().count(keyword.lower())
    return keyword_counts

# Function to visualize keyword frequency
def plot_keyword_frequency(keyword_counts):
    logging.info("Plotting keyword frequency...")
    logging.info(keyword_counts)
    plt.bar(keyword_counts.keys(), keyword_counts.values())
    plt.title('Keyword Frequency in Blog Article Titles')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.show()

# Main function
def main(urls, keywords):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_webpage, url) for url in urls]
        html_pages = [future.result() for future in futures]

    all_titles = []
    for html in html_pages:
        titles = parse_articles(html)
        all_titles.extend(titles)

    keyword_counts = count_keywords(all_titles, keywords)
    plot_keyword_frequency(keyword_counts)

if __name__ == "__main__":
    # List of URLs to scrape
    urls = [
        'https://blog.seancoughlin.me/optimizing-api-performance-best-practices-and-tools',
        'https://blog.seancoughlin.me/automating-your-development-workflow-best-practices-and-tools',
    ]

    # List of keywords to analyze
    keywords = ['api', 'microservice', 'optimize', 'engineer', 'software']

    main(urls, keywords)

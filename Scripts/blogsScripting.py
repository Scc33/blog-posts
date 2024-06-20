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
def parse_article(html):
    logging.info("Parsing articles for headers and text...")
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("article")
    titles = [
        article.find("h2").get_text() for article in articles if article.find("h2")
    ]
    # Extract all paragraph tags
    paragraph_tags = soup.find_all("p")
    # Extract and collect text from each paragraph tag
    paragraphs = [tag.get_text() for tag in paragraph_tags]
    return titles, paragraphs


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
    logging.debug(keyword_counts)
    plt.bar(keyword_counts.keys(), keyword_counts.values())
    plt.title("Keyword Frequency in Blog Article Titles")
    plt.xlabel("Keywords")
    plt.ylabel("Frequency")
    plt.show()


def adjust_for_percentage(keyword_counts):
    total = sum(keyword_counts.values())
    return {word: count / total for word, count in keyword_counts.items()}


def remove_stop_words(words):
    stop_words = set(
        [
            "a",
            "about",
            "above",
            "after",
            "again",
            "against",
            "all",
            "am",
            "an",
            "and",
            "any",
            "are",
            "aren't",
            "as",
            "at",
            "be",
            "because",
            "been",
            "before",
            "being",
            "below",
            "between",
            "both",
            "but",
            "by",
            "can",
            "can't",
            "cannot",
            "could",
            "couldn't",
            "did",
            "didn't",
            "do",
            "does",
            "doesn't",
            "doing",
            "don't",
            "down",
            "during",
            "each",
            "few",
            "for",
            "from",
            "further",
            "had",
            "hadn't",
            "has",
            "hasn't",
            "have",
            "haven't",
            "having",
            "he",
            "he'd",
            "he'll",
            "he's",
            "her",
            "here",
            "here's",
            "hers",
            "herself",
            "him",
            "himself",
            "his",
            "how",
            "how's",
            "i",
            "i'd",
            "i'll",
            "i'm",
            "i've",
            "if",
            "in",
            "into",
            "is",
            "isn't",
            "it",
            "it's",
            "its",
            "itself",
            "let's",
            "me",
            "more",
            "most",
            "mustn't",
            "my",
            "myself",
            "no",
            "nor",
            "not",
            "of",
            "off",
            "on",
            "once",
            "only",
            "or",
            "other",
            "ought",
            "our",
            "ours",
            "ourselves",
            "out",
            "over",
            "own",
            "same",
            "shan't",
            "she",
            "she'd",
            "she'll",
            "she's",
            "should",
            "shouldn't",
            "so",
            "some",
            "such",
            "than",
            "that",
            "that's",
            "the",
            "their",
            "theirs",
            "them",
            "themselves",
            "then",
            "there",
            "there's",
            "these",
            "they",
            "they'd",
            "they'll",
            "they're",
            "they've",
            "this",
            "those",
            "through",
            "to",
            "too",
            "under",
            "until",
            "up",
            "very",
            "was",
            "wasn't",
            "we",
            "we'd",
            "we'll",
            "we're",
            "we've",
            "were",
            "weren't",
            "what",
            "what's",
            "when",
            "when's",
            "where",
            "where's",
            "which",
            "while",
            "who",
            "who's",
            "whom",
            "why",
            "why's",
            "with",
            "won't",
            "would",
            "wouldn't",
            "you",
            "you'd",
            "you'll",
            "you're",
            "you've",
            "your",
            "yours",
            "yourself",
            "yourselves",
        ]
    )
    filtered_words = {word: count for word, count in words.items() if word not in stop_words}
    return filtered_words


def filter_by_percentage(keyword_counts, threshold=0.0035):
    return {word: count for word, count in keyword_counts.items() if count > threshold}


# Main function
def main(urls):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_webpage, url) for url in urls]
        html_pages = [future.result() for future in futures]

    all_titles = []
    all_text = []
    for html in html_pages:
        titles, paragraphs = parse_article(html)
        all_titles.extend(titles)
        all_text.extend(paragraphs)

    title_keyword_counts = count_keywords(all_titles)
    text_keyword_counts = count_keywords(all_text)
    logging.debug(title_keyword_counts)
    text_keyword_counts = remove_stop_words(text_keyword_counts)
    logging.debug(title_keyword_counts)
    text_percentage = adjust_for_percentage(text_keyword_counts)
    logging.debug(text_percentage)
    text_percentage_cutoff = filter_by_percentage(text_percentage)
    logging.debug(text_percentage_cutoff)
    logging.debug(title_keyword_counts)
    logging.debug(text_keyword_counts)
    plot_keyword_frequency(text_percentage_cutoff)


if __name__ == "__main__":
    urls = get_all_urls("https://blog.seancoughlin.me/")

    main(urls)

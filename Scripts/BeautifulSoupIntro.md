[python]

BeautifulSoup is a powerful library in Python for web scraping purposes. Here are some cool things you can do with BeautifulSoup:

### 1. Extracting Specific HTML Elements

You can extract specific HTML elements, such as titles, headers, links, and images.

```python
from bs4 import BeautifulSoup
import requests

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting the title of the webpage
title = soup.title.string
print("Title of the webpage:", title)

# Extracting all the headers (h1)
headers = soup.find_all('h1')
for header in headers:
    print("Header:", header.text)

# Extracting all the links
links = soup.find_all('a')
for link in links:
    print("Link text:", link.text, "| URL:", link.get('href'))

# Extracting all the images
images = soup.find_all('img')
for image in images:
    print("Image URL:", image.get('src'))
```

### 2. Navigating the DOM Tree

You can navigate the DOM tree to find elements relative to other elements.

```python
# Navigating to find siblings, parents, and children

# Finding the first paragraph
first_paragraph = soup.find('p')
print("First paragraph:", first_paragraph.text)

# Finding the next sibling of the first paragraph
next_sibling = first_paragraph.find_next_sibling()
print("Next sibling of the first paragraph:", next_sibling.text)

# Finding the parent of the first paragraph
parent = first_paragraph.find_parent()
print("Parent of the first paragraph:", parent.name)

# Finding all children of a div
div = soup.find('div')
children = div.find_all(recursive=False)  # Non-recursive
for child in children:
    print("Child of div:", child.name)
```

### 3. Searching by CSS Selectors

You can use CSS selectors to find elements.

```python
# Using CSS selectors to find elements
# Find elements with a specific class
elements_with_class = soup.select('.class-name')
for element in elements_with_class:
    print("Element with class-name:", element.text)

# Find elements with a specific id
element_with_id = soup.select_one('#id-name')
print("Element with id-name:", element_with_id.text)
```

### 4. Modifying HTML Content

You can modify the HTML content and save the changes.

```python
# Modifying HTML content
new_tag = soup.new_tag('p')
new_tag.string = "This is a new paragraph."
soup.body.append(new_tag)  # Appending the new paragraph to the body

# Saving the modified content to a new HTML file
with open('modified_example.html', 'w') as file:
    file.write(str(soup))
```

### 5. Scraping Table Data

You can extract and parse table data.

```python
# Extracting data from a table
table = soup.find('table')
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    cell_data = [cell.text.strip() for cell in cells]
    print("Row data:", cell_data)
```

### 6. Handling Pagination

You can handle pagination to scrape multiple pages of data.

```python
# Handling pagination to scrape multiple pages
base_url = 'https://example.com/page='
page = 1
while True:
    url = f"{base_url}{page}"
    response = requests.get(url)
    if response.status_code != 200:
        break  # Stop if there are no more pages
    
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract data from the current page
    articles = soup.find_all('article')
    for article in articles:
        print("Article title:", article.find('h2').text)
    
    page += 1
```

### 7. Scraping JavaScript-rendered Content

For JavaScript-rendered content, you can use `selenium` with BeautifulSoup.

```python
from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

url = 'https://example.com'
driver.get(url)

# Get the rendered HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Extract data as usual with BeautifulSoup
titles = soup.find_all('h2')
for title in titles:
    print("Title:", title.text)

driver.quit()
```

### Summary

BeautifulSoup, combined with other libraries like Requests and Selenium, provides powerful tools for web scraping. You can extract, navigate, modify, and handle web content efficiently.
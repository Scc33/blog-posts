from bs4 import BeautifulSoup
import requests

url = 'https://blog.seancoughlin.me/automating-your-development-workflow-best-practices-and-tools'
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

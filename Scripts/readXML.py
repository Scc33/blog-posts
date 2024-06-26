import xml.etree.ElementTree as ET
import re

def extract_slug(url: str) -> str:
    """Extracts the slug from a given URL."""
    match = re.search(r'https://blog\.seancoughlin\.me/([^/]+)$', url)
    if match and match.group(1) != "":
        return match.group(1)
    return ""

def process_sitemap(xml_content: str) -> list[str]:
    """Processes the sitemap and returns a list of slugs from specific URLs."""
    slugs = []
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    root = ET.fromstring(xml_content)

    for url in root.findall('ns:url', namespace):
        loc = url.find('ns:loc', namespace).text
        if 'tag/' not in loc:
            slug = extract_slug(loc)
            if slug != "":
                slugs.append(slug)
    
    return slugs

# Example XML content
xml_content = """
<Replace with XML>
"""

def clean_slugs(slugs: list[str]) -> list[str]:
    """Removes empty elements and replaces all '-' with spaces."""
    cleaned_slugs = [slug.replace("-", " ") for slug in slugs if slug]
    return cleaned_slugs

print("Running the script...")

# Process the sitemap
slugs = process_sitemap(xml_content)

cleaned_slugs = clean_slugs(slugs)

# Print the slugs
for slug in cleaned_slugs:
    print(slug)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl(start_url):
    visited = set()          # Already visited URLs
    to_visit = [start_url]   # Queue of URLs to visit
    domain = urlparse(start_url).netloc  # Domain filter

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue

        visited.add(url)
        print(f"[*] Crawling: {url}")

        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                print(f"[!] Non-200 status at {url}: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            # Find all <a href=""> links
            for link_tag in soup.find_all('a', href=True):
                href = link_tag['href']
                absolute_url = urljoin(url, href)  # Convert relative → absolute
                parsed_url = urlparse(absolute_url)

                # Only follow internal URLs (same domain)
                if parsed_url.netloc == domain and absolute_url not in visited:
                    to_visit.append(absolute_url)
        except Exception as e:
            print(f"[!] Error visiting {url}: {e}")

    return list(visited)

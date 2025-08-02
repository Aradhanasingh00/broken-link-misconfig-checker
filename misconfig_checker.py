import requests

IMPORTANT_HEADERS = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
]

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        broken = response.status_code >= 400

        missing_headers = []
        for header in IMPORTANT_HEADERS:
            if header not in response.headers:
                missing_headers.append(header)

        directory_listing = False
        if "Index of /" in response.text:
            directory_listing = True

        return {
            "url": url,
            "status_code": response.status_code,
            "broken": broken,
            "missing_headers": missing_headers,
            "directory_listing": directory_listing
        }
    except Exception as e:
        print(f"[!] Error checking {url}: {e}")
        return {
            "url": url,
            "status_code": None,
            "broken": True,
            "missing_headers": IMPORTANT_HEADERS,
            "directory_listing": False
        }

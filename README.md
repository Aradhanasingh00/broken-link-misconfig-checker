# 🛡️ Broken Links & Misconfig Checker

A lightweight Python tool that:
- Crawls a given website to find all internal pages
- Detects broken links (HTTP 404/500 etc)
- Checks for missing important security headers
- Detects if directory listing is enabled
- Generates an optional HTML report

> 📦 Built with Python 3 & BeautifulSoup, Requests, Jinja2.

---

## 🚀 Features
✅ Crawl entire domain (internal links only)  
✅ Detect broken URLs (status >= 400)  
✅ Check for missing security headers:
- `X-Frame-Options`
- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options`

✅ Detect "Index of /" (directory listing enabled)  
✅ Clean CLI summary + optional HTML report

---

## 📸 Screenshot
*(Example HTML report)*

---

## 🛠️ Installation
Clone the repository:
```bash
git clone https://github.com/Aradhanasingh00/broken-link-misconfig-checker.git
cd broken-link-misconfig-checker
## Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate
##Install dependencies:
pip install -r requirements.txt

#Usage
python3 main.py --url https://example.com --report html

Made with ❤️ by Aradhana Singh 



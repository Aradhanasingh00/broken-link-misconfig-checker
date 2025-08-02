import argparse
from crawler import crawl
from misconfig_checker import check_url
from report_generator import generate_html_report
from utils import print_summary

def main():
    parser = argparse.ArgumentParser(description="Broken Links & Misconfig Checker")
    parser.add_argument('--url', required=True, help='Start URL to crawl')
    parser.add_argument('--report', choices=['html'], help='Generate HTML report')
    args = parser.parse_args()

    print("[*] Crawling...")
    urls = crawl(args.url)
    print(f"[+] Found {len(urls)} internal URLs")

    print("[*] Checking URLs...")
    results = []
    for url in urls:
        result = check_url(url)
        results.append(result)

    print_summary(results)

    if args.report == "html":
        generate_html_report(results)

if __name__ == "__main__":
    main()

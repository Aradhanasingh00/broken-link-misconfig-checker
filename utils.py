def print_summary(results):
    total = len(results)
    broken = [r for r in results if r['broken']]
    missing = [r for r in results if r['missing_headers']]
    dirs = [r for r in results if r['directory_listing']]

    print(f"\n=== Scan Summary ===")
    print(f"Total URLs scanned: {total}")
    print(f"Broken links: {len(broken)}")
    print(f"Pages missing security headers: {len(missing)}")
    print(f"Pages with directory listing: {len(dirs)}")

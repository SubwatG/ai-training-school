import re, sys, os

def verify():
    print("=== Verification Gate 3: Site Integration & Asset Resolution ===")
    site_dir = '/home/kitti/Projects/Activities-me/ai-training-school/site'
    html_files = ['index.html', 'prompts.html', 'tutorials.html', 'showcase.html']

    errors = []

    # 1. Check HTML existence & Internal Navigation Links
    for h in html_files:
        p = os.path.join(site_dir, h)
        if not os.path.exists(p):
            errors.append(f"Missing HTML file: {h}")
            continue

        with open(p, 'r', encoding='utf-8') as fp:
            content = fp.read()

        # Check title & viewport
        if '<title>' not in content or 'viewport' not in content:
            errors.append(f"{h}: Missing title or viewport meta tag")

        # Extract internal links (href="*.html" or href="#...")
        links = re.findall(r'href="([^"#:]+(?:\.html)?(?:#[^"]*)?)"', content)
        for link in links:
            if link.startswith('http') or link.startswith('mailto:'):
                continue
            base_link = link.split('#')[0].split('?')[0]
            if base_link and not os.path.exists(os.path.join(site_dir, base_link)):
                errors.append(f"{h}: Broken link href='{link}' (file {base_link} not found)")

        # Extract img src and script src
        img_srcs = re.findall(r'src="([^":]+)"', content)
        for src in img_srcs:
            if src.startswith('http') or src.startswith('//'):
                continue
            base_src = src.split('?')[0]
            if not os.path.exists(os.path.join(site_dir, base_src)):
                errors.append(f"{h}: Broken asset src='{src}' (file not found)")

        # Check for unrendered KaTeX anomalies
        if '\\begin{equation}' in content or '\\begin{align}' in content:
            errors.append(f"{h}: Unescaped raw LaTeX block found in plain HTML")

    # 2. Check Math Bridge & Speedrun in tutorials.html
    tut_path = os.path.join(site_dir, 'tutorials.html')
    with open(tut_path, 'r', encoding='utf-8') as fp:
        tut_content = fp.read()
        if 'id="mathbidge"' not in tut_content or 'Alt + =' not in tut_content:
            errors.append("tutorials.html: Missing Math Equation Bridge section or Alt+= shortcut")
        if 'id="speedrun"' not in tut_content or '80 นาที' not in tut_content:
            errors.append("tutorials.html: Missing AI Speedrun section")

    if errors:
        print(f"[FAIL] Gate 3 failed with {len(errors)} errors:")
        for e in errors:
            print(f"  - {e}")
        return False

    print("[SUCCESS] Gate 3 Passed: 100% Valid Links, Asset paths, and Cross-site Consistency.")
    return True

if __name__ == '__main__':
    success = verify()
    sys.exit(0 if success else 1)

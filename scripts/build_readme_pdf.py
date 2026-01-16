#!/usr/bin/env python3
"""Download images from a given page, create a README copy with local
image references, and convert it to PDF using scripts/md_to_pdf_fixed.py.
"""
import os, sys
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

repo_root = os.path.abspath(os.getcwd())
page = 'https://oshwlab.com/lckfb-team/coloreasypicox'
print('Fetching', page)
r = requests.get(page, headers={'User-Agent':'Mozilla/5.0'}, timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')
imgs = [urljoin(page, img.get('src')) for img in soup.find_all('img') if img.get('src')]
print('Found', len(imgs), 'images')
docs = os.path.join(repo_root, 'docs')
os.makedirs(docs, exist_ok=True)
out_md = os.path.join(docs, 'README_with_images.md')
with open(out_md, 'w', encoding='utf-8') as f:
    f.write('# NOVA — README (with images)\n\n')
    for u in imgs:
        f.write(f'![NOVA]({u})\n\n')
    f.write('\n')
    readme = os.path.join(repo_root, 'README.md')
    if os.path.exists(readme):
        f.write('\n---\n\n')
        with open(readme, 'r', encoding='utf-8') as rfile:
            f.write(rfile.read())
print('Wrote', out_md)

conv = os.path.join(repo_root, 'scripts', 'md_to_pdf_fixed.py')
if os.path.exists(conv):
    print('Converting to PDF...')
    rc = os.system(f'python3 \"{conv}\" \"{out_md}\" \"{os.path.join(docs, \"README_with_images.pdf\")}\"')
    sys.exit(rc)
else:
    print('Converter not found:', conv)
    sys.exit(2)

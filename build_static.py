#!/usr/bin/env python
"""
Build script to generate static HTML for GitHub Pages deployment.
This script renders the Django template and copies all static assets to docs/ folder.
"""

import os
import sys
import shutil
import django
from pathlib import Path

# Directories
REPO_ROOT = Path(__file__).resolve().parent
DJANGO_DIR = REPO_ROOT / 'diego_cv'
STATIC_PAGE_SERVING_DIR = REPO_ROOT / 'static_page_serving'
STATIC_SOURCE = DJANGO_DIR / 'static'

# Add Django project to path and setup
sys.path.insert(0, str(DJANGO_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diego_cv.settings')
django.setup()

from django.template.loader import render_to_string
from django.conf import settings

# Clean and create docs directory
if STATIC_PAGE_SERVING_DIR.exists():
    shutil.rmtree(STATIC_PAGE_SERVING_DIR)
STATIC_PAGE_SERVING_DIR.mkdir()

print("Rendering Django template to static HTML...")
# Render the template
html_content = render_to_string('portfolio/home.html')

# Replace Django static tags with relative paths
html_content = html_content.replace('="/static/', '="./static/')
html_content = html_content.replace("='/static/", "='./static/")

# Write index.html
with open(STATIC_PAGE_SERVING_DIR / 'index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Created: {STATIC_PAGE_SERVING_DIR / 'index.html'}")

# Copy static files
print("\nCopying static files...")
shutil.copytree(STATIC_SOURCE, STATIC_PAGE_SERVING_DIR / 'static')
print(f"Copied static files to: {STATIC_PAGE_SERVING_DIR / 'static'}")


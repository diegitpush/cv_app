# GitHub Pages Deployment

This folder contains the static HTML version of the Django CV website for GitHub Pages deployment.

## Generated Files

- `index.html` - Static HTML generated from `diego_cv/portfolio/templates/portfolio/home.html`
- `static/` - Copy of all static assets (CSS, JS, images, PDFs)

## Rebuilding

To regenerate this folder after making changes to the Django template:

```bash
python build_static.py
```

This will automatically:
1. Render the Django template to static HTML
2. Replace Django `{% static %}` tags with relative paths
3. Copy all static assets to `docs/static/`

## Deployment

This site is deployed via GitHub Pages from the `/docs` folder.

#!/bin/bash
# chmod +x deploy.sh

# Generate the website
pelican content -s pelicanconf.py

# Deploy to GitHub Pages
ghp-import -m "Update gh-pages" -n output
git push origin gh-pages
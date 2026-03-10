# publishconf.py
import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'https://lite-system.ru'
RELATIVE_URLS = False

# Включить кэширование для production
LOAD_CONTENT_CACHE = True
DELETE_OUTPUT_DIRECTORY = False

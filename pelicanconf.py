AUTHOR = 'alaModo'
SITENAME = 'Лёгкие системы'
SITEURL = ""

DEFAULT_LANG = 'ru'
THEME = 'themes/onec'

DEFAULT_PAGINATION = False

PATH = 'content'
PAGE_PATHS = ['pages']
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}/'
INDEX_SAVE_AS = 'index.html'

# Главная страница
DIRECT_TEMPLATES = ['index']  # Активирует обработку index.html

TIMEZONE = 'Europe/Moscow'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Основные настройки
AUTHOR = 'alaModo'
SITENAME = 'Лёгкие системы'
SITEURL = ""
DEFAULT_LANG = 'ru'
TIMEZONE = 'Europe/Moscow'

# Пути и генерация страниц
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']  # Добавлено для статей/блога
STATIC_PATHS = ['images', 'extra', 'files']  # Расширенные статические пути

# URL-структура
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'articles/{slug}/'  # Добавлено для статей
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
INDEX_SAVE_AS = 'index.html'
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

# Настройки темы
THEME = 'themes/onec'
DEFAULT_PAGINATION = False

# Favicon и статические файлы
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.htaccess': {'path': '.htaccess'},
}

# Главная страница
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

# Настройки для разработки (переопределяются в publishconf.py)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Дополнительные настройки
LOAD_CONTENT_CACHE = False  # Для разработки
DELETE_OUTPUT_DIRECTORY = True  # Очищать выходную папку при сборке

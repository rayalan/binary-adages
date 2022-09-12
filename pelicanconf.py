AUTHOR = 'Alan Ray'
SITENAME = 'Binary Adages'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/alan-ray-3513aa14/'),
          #('Another social link', '#'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SLUGIFY_SOURCE = 'basename'
PLUGINS = ['extract_toc', 'neighbors', 'series']

MARKDOWN = {
    'extension_configs' : {
        'markdown.extensions.admonition': {},
        'markdown.extensions.extra': {},  # Required for Pelican
        'markdown.extensions.meta': {},  # Required for Pelican
        'markdown.extensions.codehilite': {'css_class': 'highlight'}, # Pelican default
        'markdown.extensions.toc' : {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
        'markdown.extensions.toc': {},
        'md_mermaid' : {},
        'd3ext' : {},
    },
}

# Elegant
AUTHORS = {
    'Alan Ray' : {
        'url' : '/pages/about.html',
        'blurb' : 'The Art and Science of Software Development',
        'avatar' : 'https://www.gravatar.com/avatar/1ada374ef69844ee2b619c4921891d53?s=512&d=identicon'
    },
#    a18cc4de9b361fbd9cad611d7d042c5c
}

THEME = 'elegant'

LANDING_PAGE_TITLE = 'Welcome'
RECENT_ARTICLES_COUNT = 10
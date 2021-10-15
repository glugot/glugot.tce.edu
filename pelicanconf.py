AUTHOR = 'L. Guruprasad'
SITENAME = 'GLUGOT - GNU/Linux User Group of TCE, Madurai'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

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

LINKS = (
    ('About', '/pages/about.html'),
    ('Meetings','/pages/meetings.html'),
    ('Contact', '/pages/contact.html'),
    ("FS'tival", 'https://fstival.tce.edu'),
    ('GLUG-Madurai', 'http://glug-madurai.org'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'glugot'
THEME_STATIC_DIR = 'theme'

# Custom settings for the glugot theme
SITE_DESCRIPTION = "The website for the GNU/Linux User Group of TCE, Madurai."

def get_theme_static_asset_url(file_relative_path):
    """
    Return the absolute path to the given static asset file.
    """
    return '{}/{}/{}'.format(SITEURL, THEME_STATIC_DIR, file_relative_path)


BRAND_IMAGES = (
    {'src': get_theme_static_asset_url('images/gnu-head.svg'), 'width': '64px', 'height': '64px', 'alt': 'GNU head'},
    {'src': get_theme_static_asset_url('images/tux.svg'), 'width': '64px', 'height': '64px', 'alt': 'Tux'},
)

BRAND_TEXT = 'GLUGOT'

# Speicy the order of the blocks
BLOCKS_ORDER = [
    "FS'tival '21 - Software Freedom Day",
    'Meeting announcement',
    'Join the conversation',
]

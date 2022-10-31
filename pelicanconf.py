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

LINKS = (
    ('About', '/pages/about.html'),
    ('Meetings','/pages/meetings.html'),
    ('Contact', '/pages/contact.html'),
    ("FS'tival", 'https://fstival.tce.edu'),
    ('GLUG-Madurai', 'http://glug-madurai.org'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

def get_static_asset_url(file_relative_path):
    """
    Return the absolute path to the given static asset file.
    """
    return '{}/{}'.format(SITEURL, file_relative_path)

THEME = './themes/glugot'

FAVICON_IMAGE = {
    'path': get_static_asset_url('images/favicon.png'),
    'mime_type': 'image/png',
}

# Custom settings for the glugot theme
SITE_DESCRIPTION = "The website for the GNU/Linux User Group of TCE, Madurai."

BRAND_IMAGES = (
    {'src': get_static_asset_url('images/gnu-head.svg'), 'width': '64px', 'height': '64px', 'alt': 'GNU head'},
    {'src': get_static_asset_url('images/tux.svg'), 'width': '64px', 'height': '64px', 'alt': 'Tux'},
)

BRAND_TEXT = 'GLUGOT'

# Specify the order of the blocks
BLOCKS_ORDER = [
    "FS'tival '22 - Software Freedom Day",
    'Meeting announcement',
    'Join the conversation',
]

COPYRIGHT_TEXT = 'Copyright &copy; 2021-2022 Thiagarajar College of Engineering, Madurai - 625015.'

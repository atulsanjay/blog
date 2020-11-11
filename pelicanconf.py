#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime


AUTHOR = 'Atul Sanjay'
SITENAME = "Atul Sanjay's blog"
SITEURL = ""
SITESUBTITLE = "This is where I turn data into insights"

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = [ 'extra' ,'images','pdf','figure']

RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
    #("Redken on telegram", "https://t.me/redken_bot"),
    #("RHJobs channel on TG", "https://t.me/rhjobs"),
#)

# Keep 'name' like 'twitter' with what 'FontAwesome has for putting the right icon'

SOCIAL = (
    ("Twitter", "http://twitter.com/data_atul"),
    ("github", "http://github.com/atulsanjay"),
    ("linkedin", "https://www.linkedin.com/in/atulsanjay/"),
    ("Facebook", "https://www.facebook.com/me.atulsanjay"),
    ("Instagram", "https://www.instagram.com/_atulsanjay"),
    ("Gmail", "atulsanjay1@gmail.com"),
    )

TWITTER_USERNAME = 'data_atul'
#LINKS = (
    #("Facebook", "https://t.me/redken_bot"),
    #("Instagram", "https://t.me/rhjobs"),)

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/elegant'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites']

I18N_TEMPLATES_LANG = 'en'


# Social widget


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'themes\elegant'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'tipue_search',
    'series',
    #'assets',
    'neighbors',
    'rmd_reader'
    ]


DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search','404')

I18N_TEMPLATES_LANG = 'en'

CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'



EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}


TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

SEARCH_URL = "search"

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight", "linenums": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": "true"},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
#SHARE_POST_INTRO = "Like this post? Share on:"
#COMMENTS_INTRO = ""

FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"
USE_FOLDER_AS_CATEGORY = False

SITE_UPDATED = datetime.date.today()

LANDING_PAGE_TITLE = "The data randonneur"



##  to be added in future
############################################################

#PROJECTS = [
    #{
        #"name": "Blog-o-matic",
        #"url": "https://github.com/iranzo/blog-o-matic",
        #"description": "Canned blog automation for quickly setting up a blog with Pelican",
    #},
    #{
        #"name": "Citellus",
        #"url": "https://citellus.org",
        #"description": "Troubleshooting automation tool with easy to contribute rules",
    #},
    #{
        #"name": "Pablo Iranzo Blog",
        #"url": "https://iranzo.github.io",
        #"description": "Other projects at Github website",
    #},
    #{
        #"name": "Redken Telegram BOT",
        #"url": "https://t.me/redken_bot",
        #"description": "A Telegram bot with support for Karma, RSS Feeds, Quotes, etc",
    #},
#]


########################################################

SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/3.0/" target="_blank">
    Creative Commons Attribution 3.0 International License</a>."""


RMD_READER_RENAME_PLOT='chunklabel'

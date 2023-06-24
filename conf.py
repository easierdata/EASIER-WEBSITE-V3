# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import ablog

project = 'EASIER Website'
copyright = '2023, The EASIER Data Initiative'
author = 'The EASIER Data Initiative'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_panels",
    "myst_parser",
    "nbsphinx",
]

# Syntax highlighting
pygments_style = 'default'

# Markdown support
myst_update_mathjax = False
exclude_patterns = [
    "posts/*/.ipynb_checkpoints/*",
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "./README.md",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_title = 'The EASIER Data Initiative'

html_show_sourcelink = False
html_static_path = ['_static']
html_logo = "_static/logo.png"
html_css_files = [
    "css/custom.css"
]
html_js_files = ['custom.js']

html_sidebars = {
    "**": ["index.html"],
}

html_theme_options = {
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "footer_items": ["copyright"],
    "show_toc_level": 2,
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "favicon.png"
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "favicon.png"
        },
        {
            "rel": "icon",
            "sizes": "180x180",
            "href": "favicon.png"
        }
    ]
}

html_meta = {
    'description': 'The EASIER Data Initiative develops decentralized cyberinfrastructure for efficiently, accessibly, and sustainably onloading, analyzing, and extracting large amounts of geospatial data. Concerning onloading, we are building a generalizable pipeline for heterogeneous geospatial data ingress into the Filecoin and IPFS environment.',
    'og:title': 'The EASIER Data Initiative',
    'og:description': 'The EASIER Data Initiative develops decentralized cyberinfrastructure for efficiently, accessibly, and sustainably onloading, analyzing, and extracting large amounts of geospatial data. Concerning onloading, we are building a generalizable pipeline for heterogeneous geospatial data ingress into the Filecoin and IPFS environment.',
    'og:image': 'https://pbs.twimg.com/profile_images/1574844893817491457/sWuj_YTp_400x400.jpg',
    'twitter:title': 'The EASIER Data Initiative',
    'twitter:description': 'The EASIER Data Initiative develops decentralized cyberinfrastructure for efficiently, accessibly, and sustainably onloading, analyzing, and extracting large amounts of geospatial data. Concerning onloading, we are building a generalizable pipeline for heterogeneous geospatial data ingress into the Filecoin and IPFS environment.',
    'twitter:image': 'https://pbs.twimg.com/profile_images/1574844893817491457/sWuj_YTp_400x400.jpg',
}

html_context = {
    "default_mode": "light"
}

blog_feed_fulltext = False

blog_post_pattern = "updates/*/*"
blog_path = "updates"

suppress_warnings = ["myst.header"]

exclude_patterns = []
jupyter_execute_notebooks = "off"
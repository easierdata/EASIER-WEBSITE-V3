# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# import ablog

# Compatibility shim: avoid Theme.get_config raising and returning nothing for non-[theme] sections
try:
    from sphinx.theming import Theme
    _orig_get_config = Theme.get_config

    def _safe_get_config(self, section, key=None, default=None):
        try:
            return _orig_get_config(self, section, key, default)
        except Exception:
            # If theme implementation changed or Sphinx raises for unknown sections,
            # return the provided default so templates get sensible fallbacks
            return default

    Theme.get_config = _safe_get_config
except Exception:
    # keep going if theming API is different / unavailable
    pass

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "EASIER Website"
copyright = "2025, The EASIER Data Initiative"
author = "The EASIER Data Initiative"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_panels",
    "myst_parser",
    "nbsphinx",
    "sphinxcontrib.images",
    "sphinx_new_tab_link",
    "sphinx_subfigure"
]
    # "sphinxcontrib.mermaid",

language = "en"

# Add any paths that contain templates here, relative to root directory of repo
templates_path = ["_templates"]

# -- MyST related params -------------------------------------------------
myst_enable_extensions = ["html_image", "attrs_inline", "colon_fence"]
myst_update_mathjax = False
# myst_fence_as_directive = ["mermaid"]
suppress_warnings = ["myst.header"] # Markdown support

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "**.ipynb_checkpoints**",
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "./README.md",
    "**.doctrees**",
    "**_website**",
    "**.venv**",
    "_build",
    "Thumbs.db",
    ".DS_Store"
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_title = "The EASIER Data Initiative"
html_show_sourcelink = False
html_static_path = ["_static"]
html_extra_path = ["_img"]
html_logo = "_static/logo.png"
html_css_files = ["css/custom.css"]
html_js_files = ["hideTop.js"]
html_context = {"default_mode": "light", "logo": "_static/logo.png"}

html_sidebars = {
    "**": ["index.html"],
}

html_theme_options = {
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "content_footer_items": [],
    "footer_start": ["copyright", "last-updated"],
    "footer_end": [],
    "show_toc_level": 2,
    "logo": {
      "light_image": "_static/logo.png",
      "dark_image": "_static/logo_black.png",
   }
}

html_meta = {
    "description": "The EASIER Data Initiative develops decentralized cyberinfrastructure for efficiently, accessibly, and sustainably onloading, analyzing, and extracting large amounts of geospatial data. Concerning onloading, we are building a generalizable pipeline for heterogeneous geospatial data ingress into the Filecoin and IPFS environment.",
    "og:title": "The EASIER Data Initiative",
    "og:description": "The EASIER Data Initiative develops decentralized cyberinfrastructure for efficiently, accessibly, and sustainably onloading, analyzing, and extracting large amounts of geospatial data. Concerning onloading, we are building a generalizable pipeline for heterogeneous geospatial data ingress into the Filecoin and IPFS environment.",
    "og:image": "https://pbs.twimg.com/profile_images/1574844893817491457/sWuj_YTp_400x400.jpg",
    "twitter:title": "The EASIER Data Initiative",
    "twitter:description": "The EASIER Data Initiative develops decentralized cyberinfrastructure for efficiently, accessibly, and sustainably onloading, analyzing, and extracting large amounts of geospatial data. Concerning onloading, we are building a generalizable pipeline for heterogeneous geospatial data ingress into the Filecoin and IPFS environment.",
    "twitter:image": "https://pbs.twimg.com/profile_images/1574844893817491457/sWuj_YTp_400x400.jpg",
}


# -- Blog Page Confuguration -------------------------------------------------
blog_feed_fulltext = False
blog_post_pattern = "updates/*/*"
blog_path = "./updates"
jupyter_execute_notebooks = "off"


# -- sphinxcontrib-images configuration ----------------------------------------------
# Configure sphinxcontrib-images for clickable images
# See Documentation: https://sphinxcontrib-images.readthedocs.io/en/latest
# also this article: https://dev.to/crispy-broccoli/sphinx-inserting-media-in-restructured-rest-files-2amn

images_config = {
    "backend": "LightBox2",
    "default_image_width": "100%",
    "default_show_title": "True",
    "default_group": "default",
}

# -- Ablog properties -------------------------------------------------
# Configure directories/patterns to watch for rebuilds during ablog serve -r
# ablog_rebuild_dirs = ["./updates/"]


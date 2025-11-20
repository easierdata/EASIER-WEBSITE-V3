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
    "sphinx_subfigure",
    "sphinxcontrib.mermaid",
]

language = "en"

# Add any paths that contain templates here, relative to root directory of repo
templates_path = ["_templates"]

# -- MyST related params -------------------------------------------------
myst_enable_extensions = ["html_image", "attrs_inline", "colon_fence"]
myst_update_mathjax = False
myst_fence_as_directive = ["mermaid"]
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
html_js_files = [
    "https://cdn.jsdelivr.net/npm/mermaid@11.4.0/dist/mermaid.min.js",
    "hideTop.js"
]
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

# -- Mermaid configuration -----------------------------------------------------
# Configuration for sphinxcontrib-mermaid
mermaid_output_format = "raw"  # Use 'raw' for HTML, 'png' or 'svg' for other formats
mermaid_cmd_shell = True
mermaid_pdfcrop = ""
mermaid_version = "11.4.0"   # Match the version loaded via CDN

# Disable extension's built-in zoom to avoid conflicts
mermaid_d3_zoom = True       # We'll implement our own zoom

# Mermaid initialization with D3 module import for zoom support
mermaid_init_js = """
import * as d3 from 'https://cdn.jsdelivr.net/npm/d3@7.9.0/+esm';

mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
        fontSize: '14px',
        primaryColor: '#90EE90',
        primaryTextColor: '#000000',
        primaryBorderColor: '#333333',
        lineColor: '#333333',
        secondaryColor: '#FFD700',
        tertiaryColor: '#87CEEB',
        background: '#ffffff',
        mainBkg: '#ffffff',
        nodeBkg: '#f9f9f9',
        clusterBkg: '#f5f5f5',
        edgeLabelBackground: '#ffffff'
    },
    flowchart: {
        useMaxWidth: false,
        htmlLabels: true,
        curve: 'basis'
    },
    sequence: {
        useMaxWidth: false
    },
    gantt: {
        useMaxWidth: false
    }
});

// Process pre.mermaid elements and convert to proper Mermaid diagrams
document.addEventListener('DOMContentLoaded', function() {
    // Convert pre.mermaid elements to div.mermaid for proper rendering
    const preMermaidElements = document.querySelectorAll('pre.mermaid');
    preMermaidElements.forEach(function(preElement) {
        const content = preElement.textContent.trim();
        const divElement = document.createElement('div');
        divElement.className = 'mermaid';
        divElement.textContent = content;
        preElement.parentNode.replaceChild(divElement, preElement);
    });

    // Re-initialize Mermaid to process converted elements
    if (preMermaidElements.length > 0) {
        mermaid.init(undefined, document.querySelectorAll('.mermaid'));
    }

    function addZoomToMermaids() {
        // Wait for Mermaid to render diagrams
        const mermaidElements = document.querySelectorAll('.mermaid');
        const svgElements = document.querySelectorAll('.mermaid svg');

        if (mermaidElements.length > 0 && svgElements.length === 0) {
            console.log('Mermaid elements found but not rendered yet, waiting...');
            setTimeout(addZoomToMermaids, 200);
            return;
        }

        // Apply zoom to each SVG
        svgElements.forEach(function(svgElement) {
            const svg = d3.select(svgElement);

            // Add some styling for centering and interactivity hints
            svg.style('display', 'block')
               .style('margin', '0 auto')
               .style('cursor', 'grab')
               .style('border', '1px solid #e1e5e9')
               .style('border-radius', '8px')
               .style('box-shadow', '0 2px 8px rgba(0,0,0,0.1)');

            // Wrap the content in a group for zooming
            const content = svg.select('g');
            if (content.empty()) {
                // If no existing g element, wrap all content
                const innerHTML = svg.html();
                svg.html('<g class="zoom-content">' + innerHTML + '</g>');
            }

            const zoomGroup = svg.select('g');

            // Create zoom behavior
            const zoom = d3.zoom()
                .scaleExtent([0.1, 10])
                .on('start', function() {
                    svg.style('cursor', 'grabbing');
                })
                .on('zoom', function(event) {
                    zoomGroup.attr('transform', event.transform);
                })
                .on('end', function() {
                    svg.style('cursor', 'grab');
                });

            // Apply zoom to SVG
            svg.call(zoom);

            // Add a subtle tooltip hint on first hover
            let hasShownHint = false;
            svg.on('mouseenter', function() {
                if (!hasShownHint) {
                    // Create a temporary tooltip
                    const tooltip = d3.select('body').append('div')
                        .style('position', 'absolute')
                        .style('background', 'rgba(0,0,0,0.8)')
                        .style('color', 'white')
                        .style('padding', '8px 12px')
                        .style('border-radius', '4px')
                        .style('font-size', '12px')
                        .style('pointer-events', 'none')
                        .style('z-index', '1000')
                        .text('💡 Scroll to zoom, drag to pan')
                        .style('left', (event.pageX + 10) + 'px')
                        .style('top', (event.pageY - 30) + 'px');

                    // Remove tooltip after 3 seconds
                    setTimeout(function() {
                        tooltip.transition().duration(500).style('opacity', 0).remove();
                    }, 3000);

                    hasShownHint = true;
                }
            });

            // Add reset button for zoom functionality
            const resetButton = document.createElement('button');
            resetButton.innerHTML = '⌂';
            resetButton.title = 'Reset zoom';
            resetButton.style.cssText = `
                position: absolute;
                top: 10px;
                right: 10px;
                width: 32px;
                height: 32px;
                border: 2px solid #4a90e2;
                background: linear-gradient(135deg, #4a90e2, #357abd);
                color: white;
                cursor: pointer;
                border-radius: 6px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 14px;
                font-weight: bold;
                box-shadow: 0 3px 12px rgba(74, 144, 226, 0.3), 0 1px 3px rgba(0,0,0,0.2);
                z-index: 1000;
                opacity: 0.9;
                transition: all 0.25s ease;
            `;

            // Add hover effects
            resetButton.onmouseover = function() {
                this.style.background = 'linear-gradient(135deg, #5ba0f2, #4a90e2)';
                this.style.opacity = '1';
                this.style.transform = 'scale(1.1)';
                this.style.boxShadow = '0 4px 16px rgba(74, 144, 226, 0.4), 0 2px 6px rgba(0,0,0,0.3)';
            };

            resetButton.onmouseout = function() {
                this.style.background = 'linear-gradient(135deg, #4a90e2, #357abd)';
                this.style.opacity = '0.9';
                this.style.transform = 'scale(1)';
                this.style.boxShadow = '0 3px 12px rgba(74, 144, 226, 0.3), 0 1px 3px rgba(0,0,0,0.2)';
            };            // Reset zoom on click
            resetButton.onclick = function() {
                svg.transition()
                   .duration(300)
                   .call(zoom.transform, d3.zoomIdentity);
            };

            // Make parent container relative positioned and add button
            const parentContainer = svgElement.parentNode;
            if (parentContainer.style.position !== 'relative') {
                parentContainer.style.position = 'relative';
            }
            parentContainer.appendChild(resetButton);

            console.log('Interactive zoom applied to Mermaid diagram');
        });
    }

    // Start the process
    setTimeout(addZoomToMermaids, 500);
});
"""

# Ensure Mermaid.js is loaded from CDN
# Don't use local mermaid command, use JS instead

# Optional: Add parameters for styling (used when output format is not 'raw')
mermaid_params = [
    "--theme", "default",
    # "--width", "1000",
    "--backgroundColor", "transparent"
]

# -- Ablog properties -------------------------------------------------
# Configure directories/patterns to watch for rebuilds during ablog serve -r
ablog_rebuild_dirs = ["./updates/"]


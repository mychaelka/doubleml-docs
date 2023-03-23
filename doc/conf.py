# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import doubleml


# -- Project information -----------------------------------------------------

project = 'DoubleML'
copyright = '2021, Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M.'
author = 'Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M.'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'matplotlib.sphinxext.plot_directive',
    'nbsphinx',
    'sphinx_gallery.load_style',
    'sphinx_copybutton',
    'sphinx_panels',
    'jupyter_sphinx',
]

# sphinx-panels shouldn't add bootstrap css since the pydata-sphinx-theme
# already loads it
panels_add_bootstrap_css = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'shared/*']

master_doc = 'index'

autoclass_content = 'class'
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# html_logo = '../img/logo.png'
html_extra_path = ['../img/logo.png']
html_favicon = '../img/favicon.ico'

# Define the json_url for our version switcher.
json_url = 'https://docs.doubleml.org/stable/_static/switcher.json'

# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
# If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# If it is an integer, we're in a PR build and the version isn't correct.
if not version_match or version_match.isdigit():
    # For local development, infer the version to match from the package.
    release = doubleml.__version__
    if "dev" in release or "rc" in release:
        version_match = "latest"
        # We want to keep the relative reference if we are in dev mode
        # but we want the whole url if we are effectively in a released version
        json_url = "_static/switcher.json"
    else:
        version_match = "v" + release

html_theme_options = {
    "navbar_start": ["navbar-logo", "version-switcher"],
    'github_url': 'https://github.com/DoubleML/doubleml-for-py',
    'navigation_with_keys': False,
    'switcher': {
        'json_url': json_url,
        'version_match': version_match,
    }
}

html_sidebars = {'**': ['logo.html',
                        'search-field.html',
                        'sidebar-nav-bs.html'],
                 'workflow/workflow': ['logo.html',
                                       'search-field.html',
                                       'sidebar-nav-bs.html',
                                       'sidebar-doubleml-workflow.html'],
                 'guide/guide': ['logo.html',
                                 'search-field.html',
                                 'sidebar-nav-bs.html']}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: | {2,5}\.\.\.\.:'
copybutton_prompt_is_regexp = True

# config of sphinx gallery for examples
nbsphinx_prolog = r"""
.. raw:: html
    {% raw %}
        <div class="admonition note">
        <p class="admonition-title">Note</p>
        <ul class="simple">
    {% endraw %}
    Download Jupyter notebook:
    {{ '<' }}a class={{ '"' }}reference external{{ '"' }} href={{ '"' }}https://docs.doubleml.org/stable/{{ env.doc2path(env.docname, base=None) }}{{ '"' }}{{ '>' }}https://docs.doubleml.org/stable/{{ env.doc2path(env.docname, base=None) }}{{ '</a>' }}.
    {% raw %}
        </ul>
        </div>
    {% endraw %}
"""

# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(sys.version_info), None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'statsmodels': ('https://www.statsmodels.org/stable/', None),
}

linkcheck_ignore = [
    'https://doi.org/10.1093/ectj/utaa001',  # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/ectj.12097',  # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.2307/2171802',  # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.2307/1912705',  # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1093/ectj/utaa027', # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/rssb.12026', # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1111/rssa.12623', # Valid DOI; Causes 403 Client Error: Forbidden for url:...
    'https://doi.org/10.1146/annurev-economics-012315-015826', # Valid DOI; Causes 403 Client Error: Forbidden for url:...
]

# To execute R code via jupyter-execute one needs to install the R kernel for jupyter
# https://github.com/IRkernel/IRkernel

jupyter_execute_default_kernel = 'ir'
jupyter_sphinx_linenos = False

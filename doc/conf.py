# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# %% Path setup

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# %% Project information

project = 'Xoa'
copyright = '2020, Shom/Ifremer/Actimar'
author = 'Shom/Ifremer/Actimar'

# The full version, including alpha/beta/rc tags
import xoa
release = xoa.__version__


# %% General configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    'nbsphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['xoa.']


# %% Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# %% Autosumarry
autosummary_generate = True

# %% Intersphinx
intersphinx_mapping = {
    'xarray': ('http://xarray.pydata.org/en/stable/', None),
    'cmocean': ('https://matplotlib.org/cmocean/', None),
    'configobj': ('https://configobj.readthedocs.io/en/latest/', None)
    }
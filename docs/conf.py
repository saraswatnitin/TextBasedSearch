# docs/conf.py

import os
import sys
# Add your repo's root to sys.path so Sphinx can import modules
sys.path.insert(0, os.path.abspath('..'))

project = 'TextBasedSearch'
author = 'saraswatnitin'
release = '0.1'  # update with actual release version

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',       # auto‐import docstrings
    'sphinx.ext.autosummary',   # generates summary tables
    'sphinx.ext.napoleon',      # support Google/NumPy style docstrings
    'sphinx.ext.viewcode',      # include links to source
]

templates_path = ['_templates']
exclude_patterns = []

# Output options
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Autosummary
autosummary_generate = True

# If your repo has a package __version__, pick it up:
try:
    import textbasedsearch
    version = textbasedsearch.__version__
    release = version
except ImportError:
    pass


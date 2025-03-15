import os
import sys
sys.path.insert(0, os.path.abspath('../dichotomiesolver'))

# -- Project information -----------------------------------------------------

project = 'DichotomieSolver'
author = 'Youssouphe Sow'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

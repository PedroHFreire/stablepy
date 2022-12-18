import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from stablepy import __version__

project = 'stablepy'
copyright = '2022, Your Name'
author = 'Your Name'
version = __version__
release = __version__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
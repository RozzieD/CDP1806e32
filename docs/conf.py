# conf.py - Sphinx configuration for CDP1806E-R32 docs

import os
import sys

# ✅ Ensure Python can find emulator modules in the parent directory
sys.path.insert(0, os.path.abspath(".."))

project = 'CDP1806E-R32'
author = 'RozzieD'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

# Optional: LaTeX/PDF output configuration
latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\\usepackage{fancyhdr}
\\pagestyle{fancy}
\\fancyhead[LE,RO]{CDP1806E-R32 Toolchain}
\\fancyfoot[CE,CO]{\\thepage}
''',
    'figure_align': 'H',
}

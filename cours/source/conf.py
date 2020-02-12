import sphinx_nameko_theme


project = "Cours Python"
copyright = "2020, Dimitri Merejkowsky"
author = "Dimitri Merejkowsky"


release = "0.1"
language = "fr"

templates_path = ["_templates"]
language = None
exclude_patterns = []

html_theme_path = [sphinx_nameko_theme.get_html_theme_path()]
html_theme = "nameko"
html_static_path = ["_static"]

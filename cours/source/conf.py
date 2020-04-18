import sphinx_nameko_theme


project = "Cours Python"
copyright = "2020, Dimitri Merejkowsky"
author = "Dimitri Merejkowsky"


release = "0.2"
language = "fr"

templates_path = ["_templates"]
exclude_patterns = []
keep_warnings = True

html_show_sourcelink = False
html_theme_path = [sphinx_nameko_theme.get_html_theme_path()]
html_theme = "nameko"
html_static_path = ["_static"]

project = "Programmation en Python"
copyright = "2020, Dimitri Merejkowsky"
author = "Dimitri Merejkowsky"

version = "0.3"
language = "fr"

templates_path = ["_templates"]
exclude_patterns = []
keep_warnings = True

extensions = [
    "notfound.extension",
]

notfound_context = {
    "title": "Page non trouvée",
}
notfound_urls_prefix = "/"

html_show_sourcelink = False
html_theme = "agogo"
# Don't use default "<project> <version> documentation"
html_title = project
html_static_path = ["_static"]
html_use_index = False

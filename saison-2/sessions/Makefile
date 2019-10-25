all: python-S02-E04.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

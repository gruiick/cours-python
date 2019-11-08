all: python-S02-E06.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

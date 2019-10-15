all: python-S02-E03.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

all: python-S02-E10.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

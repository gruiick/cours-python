all: python-S02-E08.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

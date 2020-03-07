all: python-S02-E11.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

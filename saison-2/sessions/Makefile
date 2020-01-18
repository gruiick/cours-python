all: python-S02-E07.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

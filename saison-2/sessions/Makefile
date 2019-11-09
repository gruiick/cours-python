all: python-S02-E05.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

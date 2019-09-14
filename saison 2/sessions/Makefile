all: python-01.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

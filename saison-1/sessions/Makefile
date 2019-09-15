all: python-14.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

all: python-02.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex -t beamer $< -o $@

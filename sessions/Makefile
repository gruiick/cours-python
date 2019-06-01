all: python-13.pdf

%.pdf: %.md
	pandoc -t beamer $< -o $@

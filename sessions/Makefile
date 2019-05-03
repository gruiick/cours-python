all: python-11.pdf

%.pdf: %.md
	pandoc -t beamer $< -o $@

all: python-09.pdf

%.pdf: %.md
	pandoc -t beamer $< -o $@

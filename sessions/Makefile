all: python-12.pdf

%.pdf: %.md
	pandoc -t beamer $< -o $@

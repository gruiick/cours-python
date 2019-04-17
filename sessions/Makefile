all: python-10.pdf

%.pdf: %.md
	pandoc -t beamer $< -o $@

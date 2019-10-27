all: ./e2l-python-classes-01.pdf

%.pdf: %.md
	pandoc --pdf-engine=xelatex $< -o $@

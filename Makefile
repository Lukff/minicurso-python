all: slides-01.html

slides-01.html : markdown/01.md
	pandoc -t revealjs -s markdown/01.md -o slides-01.html --slide-level=2

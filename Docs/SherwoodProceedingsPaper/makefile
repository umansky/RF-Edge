SRC=main

#LATEX=latex
#BIBTEX=bibtex
#VIEW=xdvi
#VFILE=$(SRC).dvi

LATEX=pdflatex
BIBTEX=bibtex
VIEW=open ###acroread
VFILE=$(SRC).pdf


all:    
	$(LATEX) ${SRC}; $(BIBTEX) ${SRC}; $(LATEX) ${SRC}; $(LATEX) ${SRC}
	###$(LATEX) ${SRC}

view:  
	$(VIEW) $(VFILE)

ps:
	dvips $(SRC) -t letter -o $(SRC).ps

pdf:
	dvips $(SRC) -t letter -o $(SRC).ps
	ps2pdf $(SRC).ps $(SRC).pdf

clean:
	rm -rf *dvi *idx *log *toc *bbl *aux *blg *out *~

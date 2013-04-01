DLSCRIPT=smrsh.py
OUTPUT=active-proposals.html

$(OUTPUT): $(DLSCRIPT)
	python $(DLSCRIPT) | pandoc -f markdown -t html -o $(OUTPUT)

all: $(OUTPUT)

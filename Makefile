MODULES = docs/steamos.rst docs/streaming.rst
HTML_MODULES = $(MODULES:.rst=.html)
CSS_INCLUDE=css/bootstrap.min.css,css/github-fork-ribbon/gh-fork-ribbon.css,css/style.css
RST2HTML=rst2html.py
TOOL_CHAIN=tools/js_attachments.py

all:
	@echo "targets: html"

%.html: %.rst
	$(RST2HTML) --stylesheet=${CSS_INCLUDE} ${FLAGS} $< $@
	${TOOL_CHAIN} $@

clean:
	rm -f ${HTML_MODULES}

html: ${HTML_MODULES}
	@echo "building html documents is done"

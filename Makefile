MODULES = docs/steamos.rst docs/streaming.rst
HTML_MODULES = $(MODULES:.rst=.html)
FLAGS="--stylesheet=css/bootstrap.min.css"
RST2HTML=rst2html.py
TOOL_CHAIN=tools/js_attachments.py

all:
	@echo "targets: html"

%.html: %.rst
	$(RST2HTML) ${FLAGS} $< > $@
	${TOOL_CHAIN} $@

clean:
	rm -f ${HTML_MODULES}

html: ${HTML_MODULES}
	@echo "done"
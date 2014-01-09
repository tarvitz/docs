#!/usr/bin/env python
"""
boosts html version with js/css extensions:
* colorbox
"""
import re
import sys

CSS_INJECTION = """
<link rel='stylesheet' href='../js/colorbox/example3/colorbox.css' />
"""
JS_INJECTION = """
<script type='text/javascript' src='../js/jquery-1.8.3.min.js'></script>
<script type='text/javascript' src='../js/colorbox/jquery.colorbox-min.js'></script>

<script type='text/javascript'>
	$(document).ready(function(){
		$(".image-reference").colorbox({rel: ".image-reference"});
	});
</script>
"""

def usage():
	print("%s <file.html>" % sys.argv[0])
	sys.exit(-1)

def insert_into(base, substr, index=0):
	"""
	inserts substr into base string with given index
	
	>>> insert_into("test", "me ")
	'me test'
	>>> insert_into("test", "me ", index=3)
	'tesme t'
	"""

	return base[:index] + substr + base[index:]

def main():
	if len(sys.argv) < 2:
		usage()
	document = open(sys.argv[1]).read()
	idx = document.index('</body>')
	document = insert_into(document, JS_INJECTION, idx)
	idx = document.index('</head>')
	document = insert_into(document, CSS_INJECTION, idx)
	open(sys.argv[1], 'w').write(document)

if __name__ == '__main__':
	main()

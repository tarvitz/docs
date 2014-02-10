#!/usr/bin/env python
"""
boosts html version with js/css extensions::

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

FORK_ME_ON = """
    <div class="github-fork-ribbon-wrapper right">
        <div class="github-fork-ribbon bg-black">
            <a href="https://github.com/tarvitz/docs">Fork me on GitHub</a>
        </div>
    </div>
    <div class="github-fork-ribbon-wrapper left">
        <div class="github-fork-ribbon">
            <a href="https://github.com/tarvitz/docs">Читай на <img src='../thirdparty/stopgame.png'>StopGame</a>
        </div>
    </div>
"""


def usage():
    print("%s <file.html> [file2.html file3.html .. file_n.html]"
          % sys.argv[0])
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
    for i in xrange(1, len(sys.argv)):
        document = open(sys.argv[i]).read()
        body_close_idx = document.index('</body>')
        document = insert_into(document, JS_INJECTION, body_close_idx)
        head_close_idx = document.index('</head>')
        document = insert_into(document, CSS_INJECTION, head_close_idx)
        open(sys.argv[i], 'w').write(document)

if __name__ == '__main__':
    main()

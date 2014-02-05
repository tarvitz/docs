Docs
====
SteamOS, In-home streaming and other useful pop-articles documentation and tools for its building
.. contents:: :local:
    :depth: 3

Dependencies
------------
If you want to process ``rst`` files you would probably need some rst parser
and other document format generator based on rst. This project already includes
almost everything you would need to build html documents with bootstrap markup inside.

Although you're free to use your own instruments for building rst2html, rst2pdf and so on.

Project dependencies
~~~~~~~~~~~~~~~~~~~~
requried::

    * python-2.6, python-3.x
    * rst2pdf (*and its dependencies*)
    * PIL or Pillow (for simple watermark script use)

optional::

    * virtualenv
    * pip

Build tools installation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    user@localhost$ virtualenv --no-site-packages venv
    user@localhost$ source venv/bin/activate
    user@localhost$ pip install -r requirements/doc.txt
    user@localhost$ pip install -r requirements/tools.txt

Build documentation
~~~~~~~~~~~~~~~~~~~
You can use ``make html`` for documentation build. It uses standard C-way files building so there's no need to rebuild
whole documents storage everytime.
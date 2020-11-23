sylk parser
==============

.. image::
    https://secure.travis-ci.org/majerteam/sylk_parser.png?branch=master
   :target: http://travis-ci.org/majerteam/sylk_parser
   :alt: Travis-ci: continuous integration status.

A .slk files parser

SLK format : https://en.wikipedia.org/wiki/SYmbolic_LinK_(SYLK)

Largely inspired by : https://github.com/smontanaro/python-bits/blob/master/sylk.py

Installation
-------------

.. code-block: console

    pip install sylk_parser


Usage
------

From Python code

.. code-block:: python

    from io import StringIO
    from sylk_parser import SylkParser

    parser = SylkParser("somefile.slk")

    fbuf = StringIO()
    parser.to_csv(fbuf)

    test_results = fbuf.getvalue()
    print test_results


Note on dates
--------------

Dates in Sylk files are non standard offsets.
We try to find the good offset regarding the "ID" field.

See :sylk_parser.sylk.SYLK._id_field method

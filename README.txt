sylk parser
==============

A .slk files parser

SLK format : https://en.wikipedia.org/wiki/SYmbolic_LinK_(SYLK)

Largely inspired by : https://github.com/smontanaro/python-bits/blob/master/sylk.py

Installation
-------------

.. code-block: console

    pip install sylk_parser


Usage
------

From python code

.. code-block:: python

    from sylk_parser import SylkParser

    parser = SylkParser(filepath)
    with open("/tmp/result.csv", "wb") as fbuf:
        parser.to_csv(fbuf)

# -*- coding:utf-8 -*-
import csv
from sylk import SYLK
import io
import cStringIO

SYLK_CHARSET = "cp1252"


class SylkParser:

    def __init__(self, filename, headers=None):
        if headers is None:
            headers = []

        self.headers = headers
        self.sylk_handler = SYLK()
        with io.open(filename, encoding=SYLK_CHARSET) as handle:
            self.sylk_handler.parse(handle)

    def to_csv(self, fbuf, quotechar='"', delimiter=','):
        csvwriter = csv.writer(
            fbuf,
            quotechar=quotechar,
            delimiter=delimiter,
            lineterminator="\n",
            quoting=csv.QUOTE_ALL
        )

        if self.headers:
            csvwriter.writerow(self.headers)

        for line in self.sylk_handler.stream_rows():
            csvwriter.writerow(line)

    def __enter__(self):
        self.fbuf = cStringIO.StringIO()
        self.to_csv(self.fbuf)
        self.fbuf.seek(0)
        return self.fbuf

    def __exit__(self, exc, exc_val, exc_tb):
        self.fbuf.close()

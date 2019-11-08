# -*- coding:utf-8 -*-
import csv
from sylk_parser.sylk import SYLK

SYLK_CHARSET = "cp1252"


class SylkParser:

    def __init__(
        self,
        filename,
        headers=None,
        encoding=SYLK_CHARSET,
    ):
        if headers is None:
            headers = []

        self.headers = headers
        self.sylk_handler = SYLK()
        with open(filename, encoding=encoding) as handle:
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

    def _get_line_as_dict(self, line):
        """
        Transform a line (array) in a dict
        :param list line: The line
        :rtype: dict
        """
        return dict(zip(line, self.headers))

    def __iter__(self):
        for line in self.sylk_handler.stream_rows():
            if self.headers:
                yield dict(zip(self.headers, line))
            else:
                yield line

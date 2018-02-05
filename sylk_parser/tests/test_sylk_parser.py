import os
from cStringIO import StringIO
from sylk_parser import SylkParser
from sylk_parser.sylk import SYLK


def get_data_path(filename):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'datas')
    return os.path.join(path, filename)

def _test_one(test_filename, expected_results_filename, headers=None,
              encoding='cp1252'):

    filepath = get_data_path(test_filename)
    expected_results_filepath = get_data_path(expected_results_filename)

    if headers is None:
        headers = []

    parser = SylkParser(filepath, headers=headers, encoding=encoding)
    fbuf = StringIO()
    parser.to_csv(fbuf)
    test_results = fbuf.getvalue()
    with open(expected_results_filepath) as handle:
        expected_results = handle.read()
    assert test_results.strip() == expected_results.strip()
    print("Tested {}".format(test_filename))


def test_to_csv():
    _test_one(
        "wikipedia.slk",
        "wikipedia.csv",
        encoding='utf-8',
    )
    headers = ["Utilisateur", "MotDePasse"]
    _test_one(
        "libreoffice.slk",
        "libreoffice.csv",
        headers=headers,
        encoding='utf-8',
    )
    _test_one(
        "balance_analytique.slk",
        "balance_analytique.csv",
        encoding='utf-8',
    )
    _test_one(
        "balance_analytique_cp1252.slk",
        "balance_analytique.csv",
        encoding="cp1252",
    )


def test_stream_unicode():
    fpath = get_data_path("balance_analytique_cp1252.slk")
    parser = SylkParser(fpath, use_unicode=True)
    for line in parser:
        for i in line:
            assert isinstance(i, unicode)
    parser = SylkParser(fpath, use_unicode=False)
    for line in parser:
        for i in line:
            assert isinstance(i, str)


def test_detect_datebase():
    handler = SYLK()
    assert handler.datebase == handler.unixepoch
    handler.parseline("ID;P Sage")
    assert handler.datebase == handler.pcepoch

from cStringIO import StringIO
from sylk_parser import SylkParser


def _test_one(test_filename, expected_results_filename, headers=None,
              encoding='cp1252'):
    if headers is None:
        headers = []
    parser = SylkParser(test_filename, headers=headers, encoding=encoding)
    fbuf = StringIO()
    parser.to_csv(fbuf)
    test_results = fbuf.getvalue()
    with open(expected_results_filename) as handle:
        expected_results = handle.read()
    assert test_results.strip() == expected_results.strip()
    print("Tested {}".format(test_filename))


def test_to_csv():
    _test_one(
        "datas/wikipedia.slk",
        "datas/wikipedia.csv",
        encoding='utf-8',
    )
    headers = ["Utilisateur", "MotDePasse"]
    _test_one(
        "datas/libreoffice.slk",
        "datas/libreoffice.csv",
        headers=headers,
        encoding='utf-8',
    )
    _test_one(
        "datas/balance_analytique.slk",
        "datas/balance_analytique.csv",
        encoding='utf-8',
    )
    _test_one(
        "datas/balance_analytique_cp1252.slk",
        "datas/balance_analytique.csv",
        encoding="cp1252",
    )


def test_stream_unicode():
    parser = SylkParser("datas/balance_analytique_cp1252.slk", use_unicode=True)
    for line in parser:
        for i in line:
            assert isinstance(i, unicode)
    parser = SylkParser("datas/balance_analytique_cp1252.slk", use_unicode=False)
    for line in parser:
        for i in line:
            assert isinstance(i, str)

from io import StringIO
from sylk_parser import SylkParser


def test_one(test_filename, expected_results_filename, headers=None):
    if headers is None:
        headers = []
    parser = SylkParser(test_filename, headers=headers)
    fbuf = StringIO()
    parser.to_csv(fbuf)
    test_results = fbuf.getvalue()
    with open(expected_results_filename) as handle:
        expected_results = handle.read()
    assert test_results.strip() == expected_results.strip()
    print("Tested {}".format(test_filename))

test_one("tests/wikipedia.slk", "tests/wikipedia.csv")
headers = ["Utilisateur", "MotDePasse"]
test_one("tests/libreoffice.slk", "tests/libreoffice.csv", headers=headers)

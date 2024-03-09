from twttr import shorten

def test_numbers():
    assert shorten("1") == "1"
    assert shorten("0") == "0"
    assert shorten("-1") == "-1"

def test_consonants():
    assert shorten("K") == "K"
    assert shorten("ß") == "ß"
    assert shorten("k") == "k"
    assert shorten("m") == "m"
    assert shorten("V") == "V"


def test_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_punctuation():
    assert shorten(",.-?!") == ",.-?!"


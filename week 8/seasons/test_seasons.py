from seasons import convert
import pytest

def test_convert():
    assert convert(2022, 11, 28) == "Five hundred twenty-five thousand, six hundred"

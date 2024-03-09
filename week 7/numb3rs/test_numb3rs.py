from numb3rs import validate

def test_validate_num():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.256.256.256") == False
    assert validate("1000.1000.1000.1000") == False

def test_validate_alpha():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False

def test_validate_length():
    assert validate("123.123.123") == False
    assert validate("123.") == False
    assert validate("123.123.123.123.123") == False
    assert validate("123.123.123.123") == True

def test_validate_first_byte():
    assert validate("123.256.256.256") == False

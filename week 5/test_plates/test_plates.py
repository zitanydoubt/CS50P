from plates import is_valid

def test_start():
    assert is_valid("CE") == True
    assert is_valid("E4") == False
    assert is_valid("52") == False

def test_size():
    assert is_valid("CE") == True
    assert is_valid("CE1") == True
    assert is_valid("CE12") == True
    assert is_valid("CE123") == True
    assert is_valid("CE1234") == True
    assert is_valid("CE12345") == False
    assert is_valid("CE0123") == False

def test_middle():
    assert is_valid("CE1234") == True
    assert is_valid("CEE123") == True
    assert is_valid("CEEE23") == True
    assert is_valid("CEEEE1") == True
    assert is_valid("CE12EE") == False
    assert is_valid("CE1E2E") == False

def test_punctuation():
    assert is_valid("CE!.?&") == False
    assert is_valid("CE.   ") == False

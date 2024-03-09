from bank import value

def test_hello():
    assert value("Hello, Bank") == 0
    assert value("Hello, World") == 0
    assert value("Hello, David") == 0
    assert value("hello, david")  == 0


def test_h():
    assert value("Hey") == 20
    assert value("how you doing") == 20
    assert value("hi, world") == 20
    assert value("hola") == 20

def test_otherwise():
    assert value("What's up?") == 100
    assert value("what's going on?") == 100
    assert value("Well, hello!") == 100


from working import convert
import pytest

def test_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:45 AM to 5:45 PM") == "09:45 to 17:45"
    with pytest.raises(ValueError):
        assert convert("9.66 AM to 5.66 PM")
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"

def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        assert convert("13 AM to 13 PM")
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

def test_format():
    with pytest.raises(ValueError):
        assert convert("AM to PM")
    with pytest.raises(ValueError):
        assert convert("9AM to 5PM")
    with pytest.raises(ValueError):
        assert convert("9 AM 5 PM")

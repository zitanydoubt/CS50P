from um import count

def test_count_words():
    assert count("Umbridge's umbilical chord is umbriferous") == 0
    assert count("umbrella umami umbrae") == 0
    assert count("clumsy drum players") == 0
    assert count("spectrum aluminium momentum") == 0

def test_count_spaces_signs():
    assert count("um, umm, um") == 2
    assert count("um. um?") == 2
    assert count(".um.um.") == 2
    assert count("um") == 1

def test_count():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um um um") == 3
    assert count("um um um um") == 4
    assert count("UM") == 1
    assert count("UM UM UM") == 3

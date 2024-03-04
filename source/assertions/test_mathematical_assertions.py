from tests.mathematical import is_bigger, is_smaller, is_equal

def test_is_bigger():
    assert is_bigger(5, 3), "5 is bigger than 3"

def test_is_smaller():
    assert is_smaller(2, 5), "2 is smaller than 5"

def test_is_equal():
    assert is_equal(4, 4), "4 is equal to 4"
from tests.dictionary_checks import is_key_in_dictionary, is_value_in_dictionary

def test_is_key_in_dictionary():
    key = "name"
    # sample dictionary
    dictionary = {
        "name": "John",
        "age": 30,
        "job": "developer",
        "address": {
            "city": "New York",
            "zip": 10001
        }
    }
    assert is_key_in_dictionary(key, dictionary), f"The key {key} is not in {dictionary}"

def test_is_value_in_dictionary():
    value = {
            "city": "New York",
            "zip": 10001
        }
    # sample dictionary
    dictionary = {
        "name": "John",
        "age": 30,
        "job": "developer",
        "address": {
            "city": "New York",
            "zip": 10001
        }
    }
    assert is_value_in_dictionary(value, dictionary), f"The value {value} is not in {dictionary}"


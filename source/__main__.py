from assertions.test_mathematical_assertions import test_is_bigger, test_is_smaller, test_is_equal
from assertions.test_list_assertions import test_value_in_list
from assertions.test_dictionary_assertions import test_is_key_in_dictionary, test_is_value_in_dictionary

if __name__ == "__main__":
    test_is_bigger()
    test_is_smaller()
    test_is_equal()

    test_value_in_list()

    test_is_key_in_dictionary()
    test_is_value_in_dictionary()
    
    print("All tests passed!")
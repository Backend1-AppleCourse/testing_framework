from tests.list_checks import check_value_in_list

def test_value_in_list():
    value = [3]
    list_of_values = [1, 2, [3], 4, 5]
    assert check_value_in_list(value, list_of_values), f"{value} is not in {list_of_values}"
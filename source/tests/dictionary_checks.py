
def is_key_in_dictionary(key, dictionary):
    return key in dictionary

def is_value_in_dictionary(value, dictionary):
    for k, v in dictionary.items():
        if v == value:
            return True
        if isinstance(v, dict):
            if is_value_in_dictionary(value, v):
                return True
    return False
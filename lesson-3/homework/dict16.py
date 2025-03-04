def has_nested_dictionaries(dictionary):
    for value in dictionary.values():
        if type(value) == dict:
            return True
    return False

my_dict = {"name": "Dilrabo", "details": {"age": 100}}
print(has_nested_dictionaries(my_dict))
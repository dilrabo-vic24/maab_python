def filter_by_value(dictionary, condition):
    return {key: value for key, value in dictionary.items() if condition(value)}

my_dict = {"a": 1, "b": 2, "c": 3}

print(filter_by_value(my_dict, lambda x: x > 1))
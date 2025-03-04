def find_keys_with_value(dictionary, value):
    return [key for key, val in dictionary.items() if val == value]

my_dict = {"number1": 1, "number2": 2, "number3": 1}
print(find_keys_with_value(my_dict, 1)) 
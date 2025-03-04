def count_value_occurrences(dictionary, value):
    return list(dictionary.values()).count(value)

my_dict = {"number1": 1, "number2": 2, "number3": 1}
print(f"Occurance times: {count_value_occurrences(my_dict, 1)}")
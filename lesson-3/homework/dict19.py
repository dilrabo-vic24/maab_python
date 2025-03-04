def count_unique_values(dictionary):
    return len(set(dictionary.values()))

my_dict = {"a": 1, "b": 2, "c": 1}
print(count_unique_values(my_dict))
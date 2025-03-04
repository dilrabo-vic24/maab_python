def sort_dictionary_by_key(dictionary):
    sorted_dict = {}
    for key in sorted(dictionary):
        sorted_dict[key] = dictionary[key]
    return sorted_dict

my_dict = {"b": 2, "a": 1, "c": 3}
print(sort_dictionary_by_key(my_dict))
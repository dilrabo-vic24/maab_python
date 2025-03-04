def sort_dictionary_by_value(dictionary):

    items = list(dictionary.items())
    print(items)
    items.sort(key=lambda item: item[1])
    sorted_dict = {}
    for key, value in items:
        sorted_dict[key] = value
    return sorted_dict

my_dict = {"a": 3, "b": 1, "c": 2}
print(sort_dictionary_by_value(my_dict))
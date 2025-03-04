def get_value(dictionary, key):
    return dictionary.get(key, None)


my_dict = {"name": "Dilrabo ", "age": 100}
print(get_value(my_dict, "name"))
print(get_value(my_dict, "address"))
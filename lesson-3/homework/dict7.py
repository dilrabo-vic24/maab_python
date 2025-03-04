def remove_key(dictionary, key):
    dictionary.pop(key, None)
    return dictionary

my_dict = {"name": "Dilrabo", "age": 100}
print(remove_key(my_dict, "addresss"))
print(remove_key(my_dict, "age"))

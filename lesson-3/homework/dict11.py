def update_value(dictionary, key, new_value):
    dictionary[key] = new_value
    return dictionary

my_dict = {"name": "Dilrabo", "age": 100}
print(my_dict)

print(update_value(my_dict, "age", 30))
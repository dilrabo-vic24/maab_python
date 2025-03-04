def is_empty(dictionary):
    return not bool(dictionary)

my_dict1 = {}
my_dict2 = {"name": "Dilrabo", "age": 100}

print(is_empty(my_dict1))
print(is_empty(my_dict2))

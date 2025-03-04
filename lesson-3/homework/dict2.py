def check_key(dictionary, key):
    return key in dictionary

my_dict = {"name": "Dilrabo", "age": 25}
print(check_key(my_dict, "name")) 
print(check_key(my_dict, "address")) 
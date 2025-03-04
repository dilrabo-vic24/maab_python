def get_key_value_pair(dictionary, key):
    if key in dictionary:
        return (key, dictionary[key])
    return None

my_dict = {"name": "Dilrabo", "age": 100}
print(get_key_value_pair(my_dict, "name"))  
print(get_key_value_pair(my_dict, "address"))
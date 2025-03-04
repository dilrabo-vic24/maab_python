def get_first_key_value_pair(dictionary):
    for key, value in dictionary.items():
        return (key, value)
    return None

my_dict = {"name": "Dilrabo", "age": 100}
print(get_first_key_value_pair(my_dict)) 

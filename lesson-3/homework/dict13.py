def invert_dictionary(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    return inverted_dict

my_dict = {"name": "Dilrabo", "age": 100}
print(invert_dictionary(my_dict))
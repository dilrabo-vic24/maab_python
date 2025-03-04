def create_dictionary_from_lists(keys, values):
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict

keys = ["name", "age"]
values = ["Dilrabo", 100]
print(create_dictionary_from_lists(keys, values)) 
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {"name": "Dilrabo"}
dict2 = {"age": 100}
print(merge_dictionaries(dict1, dict2))
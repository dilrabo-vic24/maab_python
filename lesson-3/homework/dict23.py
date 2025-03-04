def check_common_keys(dict1, dict2):
    for key in dict1:
        if key in dict2:
            return True
    return False

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(check_common_keys(dict1, dict2))
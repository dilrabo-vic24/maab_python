def get_nested_value(dictionary):

    if "details" in dictionary and "age" in dictionary["details"]:
        return dictionary["details"]["age"]
    return None

my_dict = {"name": "Dilrabo", "details": {"age": 100}}
print(get_nested_value(my_dict))
from collections import defaultdict

def create_default_dictionary(default_value):
    return defaultdict(lambda: default_value)

my_dict = create_default_dictionary(0)

my_dict["a"] = 1
print(my_dict["b"]) 
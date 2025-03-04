def get_unique_ordered(lst):
    new_list = []

    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list


my_list = [7, 2, 7, 3, 7, 3, 5]
print(f"New list: {get_unique_ordered(my_list)}")
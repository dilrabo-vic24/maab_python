def merge_and_sort_list(list1: list, list2:list)->list:
    new_list = list1 + list2

    new_list.sort()

    return new_list


list1 = [10, 4, 5, 9]
list2 = [8, 9, 3, 1]

new_list = merge_and_sort_list(list1 = list1, list2 = list2)
print(f"New list: {new_list}")
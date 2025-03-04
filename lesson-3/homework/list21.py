def second_smallest(lst: list) -> float:

    if len(set(lst)) < 2:
        return None

    unique_sorted_lst = sorted(list(set(lst)))
    return unique_sorted_lst[1]

lst = [4, 6, 7, 9, 3, 5, 6, 7]
second_min_number  = second_smallest(lst)

print(f"Second min number: {second_min_number}")
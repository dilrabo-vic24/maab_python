def second_largest(lst: list) -> float:

    if len(set(lst)) < 2:
        return None

    unique_sorted_lst = sorted(list(set(lst)))
    return unique_sorted_lst[-2]

lst = [4, 6, 7, 9, 3, 5, 6, 7]
second_max_number  = second_largest(lst)

print(f"Second max number: {second_max_number}")
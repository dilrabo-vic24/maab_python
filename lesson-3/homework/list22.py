def filter_even_number(lst: list) -> list:
    even_numbers = []
    for i in lst:
        if not i % 2:
            even_numbers.append(i)
    
    return even_numbers

lst = [4 ,6, 7, 5, 2, 3, 1]

even_numbers = filter_even_number(lst)
print(f"Even numbers list: {even_numbers}")

def filter_odd_number(lst: list) -> list:
    odd_numbers = []
    for i in lst:
        if i % 2:
            odd_numbers.append(i)
    
    return odd_numbers

lst = [4 ,6, 7, 5, 2, 3, 1]

odd_numbers = filter_odd_number(lst)
print(f"Odd numbers list: {odd_numbers}")

def sum_of_negative(lst: list[float]) -> float:
    summa = 0
    
    for i in lst:
        if i < 0:
            summa += i

    return summa


lst = [1, -5, 7, 2, 6, -2]

print(f"Sum of negative numbers: {sum_of_negative(lst)}")
def sum_of_positive(lst: float):
    summa = 0
    for i in lst:
        if i > 0:
            summa += i
    
    return summa

lst = [1, -5, 7, 2, 6, -2]

print(f"Sum of positive numbers: {sum_of_positive(lst)}")
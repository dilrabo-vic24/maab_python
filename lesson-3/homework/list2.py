def sum_of_list(lst: list):
    summa = 0
    for i in lst:
        summa += i
    return summa


lst = [1, 2, 3, 4, 5, 6, 7]
print(f"Summa(sum_of_list): {sum_of_list(lst)}")
print(f"Summa(python function): {sum(lst)}")
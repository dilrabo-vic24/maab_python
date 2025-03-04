def count_occurances(lst: list, number: float)-> int:
    count = 0
    for i in lst:
        if(i == number):
            count += 1
    return count

lst = [1, 4, 5,3, 5, 6]
number = 5

result = count_occurances(lst, 5)
if(result == 0):
    print("Number is not in list")
else:
    print(f"Occurances time {result}")
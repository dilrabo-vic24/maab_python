list1 = [1, 1, 2]
list2 = [2, 3, 4]

result = list1[0:2]

for item in list2:
    if item not in list1:
        result.append(item)

print(result)
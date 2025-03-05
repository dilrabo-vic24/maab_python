#Nested for sikli - bu bir for siklining ichida boshqa for sikli bo'lishi. Ichki sikl tashqi siklning har bir iteratsiyasi uchun to'liq bajariladi.


for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
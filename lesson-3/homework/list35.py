def create_number_list(start:float, end: int)->list:
    if(start > end):
        return None
    return list(range(start, end))


print(f"Created list: {create_number_list(1, 10)}")
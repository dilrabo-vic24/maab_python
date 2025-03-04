def create_number_tuple(start: float, end: int) -> tuple:

    if start > end:
        return None
    return tuple(range(int(start), end))


print(f"Created tuple: {create_number_tuple(1.0, 10)}")
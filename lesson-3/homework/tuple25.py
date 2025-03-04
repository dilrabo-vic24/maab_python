def get_unique_ordered_tuple(tup):

    new_tup = ()
    for item in tup:
        if item not in new_tup:
            new_tup += (item,)
    return new_tup


my_tuple = (7, 2, 7, 3, 7, 3, 5)
print(f"New tuple: {get_unique_ordered_tuple(my_tuple)}")
def check_subset(set1: set, set2:set) -> None:

    if set1.issubset(set2):
        print("Set1 is subset of set2")
    elif set2.issubset(set1):
        print("Set2 is subset of set1")

set_1 = {1, 2}
set_2 = {1, 2, 3}
check_subset(set1=set_1, set2= set_2)
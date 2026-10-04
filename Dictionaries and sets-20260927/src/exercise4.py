def has_odd(set: set[int]) -> bool:
    for elem in set:
        if elem % 2 != 0:
            return True
    return False

def is_1_to_1(dict: dict[str, str]) -> bool:

    if len(set(dict)) != len(dict.values()):
        return False
    elif len(set(dict)) == len(dict.values()):
        return True
    else:
        return None


def printResult(result: bool, dict: dict[str, str]) -> None:
    if result or dict == {}:
        print(f"Dictionary: {dict} have unique entries.")
    elif not result:
        print(f"Dictionary: {dict} does not have unique entries.")
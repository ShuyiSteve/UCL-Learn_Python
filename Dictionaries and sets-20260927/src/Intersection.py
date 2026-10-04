def Intersection(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    Intersection = {}
    keys = dict1.keys().intersection(dict2.keys())
    for key in keys: 
        if dict1[key] == dict2[key]:
            Intersection[key] = dict1[key]
    return Intersection

def printIntersection(intersection: dict[str, int]) -> None:
    print(f"Intersection: {intersection}")
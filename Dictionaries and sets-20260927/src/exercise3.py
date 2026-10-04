import random


def max_occurences() :
    list = []
    dict = {}

    for i in range(100): 
        num = random.randint(0, 9)
        list.append(num)
    print(list)

    for elem in list:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1

    mode = max(dict, key=dict.get)
    print(f"Number {mode} appears most frequently - {max(dict.values())}  times.")

max_occurences()
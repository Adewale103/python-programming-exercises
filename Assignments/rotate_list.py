def rotate(list_, integer):
    empty_list = []
    for i in range(len(list_) - integer, len(list_)):
        empty_list.append(list_[i])
    for i in range(0, len(list_) - integer):
        empty_list.append(list_[i])
    return empty_list


lst = [2, 3, 4, 5, 6]
number = 2
print(rotate(lst, number))


def rotate_list(list_, integerr):
    if integerr > 5:
        integer = integerr % len(list_)
    else:
        integer = integerr
    return list_[-integer:] + list_[:-integer]


lst = [2, 3, 4, 5, 6]
number = 7
print(rotate_list(lst, number))

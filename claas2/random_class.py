# import random
#
# print(random.randint(1, 100))
# print(random.randrange(1, 10, 2))
# print(random.random())
# list_ = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(list_)
# print(list_)
# print(random.choice(list_))

def get_digit(number, position):
    '''return digit at position in number, counting from right'''
    assert 4 == 2, "4 is not equal 2"
    return number // (10**position) % 10

print(get_digit(234,2))
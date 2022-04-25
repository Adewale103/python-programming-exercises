# list comprehension
# lst = []
# for i in range(1, 11):
#     lst.append(i ** 2)
# print(lst)
#
# list_ = [i ** 2 for i in range(1, 11)]
# print(list_)
#
import sys

even_list_ = [i for i in range(2, 11, 2)]
print(even_list_)


#
# another_list = [num if num % 2 == 0 else num**2 for num in range(1, 11)]
# print(another_list)
#
# lst_input = [int(input("Enter a number: ")) for i in range(1, 4)]
# print(lst_input)

# list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
# print(list_nested_for)
#
# length_names = [len(name) for name in ['wale', 'adebayo', 'funmilayo', 'yemi']]
# print(length_names)
#
# upper_names = [name.upper() for name in ['wale', 'adebayo', 'funmilayo', 'yemi']]
# print(upper_names)
#
# # lists of dictionary
# list_of_dicts = [{key: value} for key, value in zip(upper_names, even_list_)]
# print(list_of_dicts)

def get_first(s: str) -> str:
    return s[0]


l = [get_first(val) for val in ["Hello", "Wale", "Fine", "Boy"]]
print(l)
# generator and list comprehension
generator = (num for num in range(1, 10 ** 5))
lst_comprehension = [num for num in range(1, 10 ** 5)]
set_comprehension = {num for num in range(1, 10 ** 5)}
# dict_comprehension = {k: v for k, v in zip(range(1, 10 ** 5))}

print(sys.getsizeof(lst_comprehension))
print(sys.getsizeof(generator))
print(sys.getsizeof(set_comprehension))
# print(sys.getsizeof(dict_comprehension))


s1 = {1, 2, 3, 5}
s2 = {4, 3, 2, 5}

s1.pop()
print("pop", s1)

# intersection
print(s1 & s2)

# intersection update
s1 &= s2
# or
s1 = s1 & s2
print(s1)

# union
print(s1 | s2)

# update
s1 |= s2
print(s1)

s1 = {1, 2, 3, 5}
s2 = {4, 3, 2, 5}
print(s1 - s2)

print(s1 ^ s2)

# subset and superset
s1 = {1, 2, 3, 5}
s2 = {1, 2, 5}
print(s1 > s2)
print(s1 < s2)

dict_play = {"name": "Tolani", "age": 32, "influenced": "Samson"}
print(dict_play["name"])

# if name not found, return argument in get
dict = {"age": 32, "influenced": "Samson"}
print(dict.get("name", "Samson"))

dict.pop("age")

dict.update()

dict.popitem()
# iterating keys for empty dictionary {}
print({}.fromkeys("hello", "UNKNOWN"))

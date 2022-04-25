num = 1


# def func():
#     global num
#     num+= 1
#     print(num)
# print(num)

# def func1():
#     num = 1
#     def func2():
#         num = 1
#         print(num)

# def add(a: int = 2, b: str = "colour") -> tuple[int, str]:
#     return a, b
#
#
# print(add(3, "3"))
# print(add(3))
# print(add())
#
# print(add(b="you", a=5))
#
# def weird(a = None):
#     if a is None:
#         a = []
#     a.append('python')
#     return a
#
# print(weird())
# print(weird([1,2,4]))
# print()

# def add(*args):
#     total = 0
#     for i in args:
#         total = total + i
#     return total
#
#
# print(add(*[1, 2, 3, 4, 5, 6, 6, 67, 7, 7]))
# lst = [45,56,77,54,22,21]
# print(add(*lst))

# def dict_pack_unpack(**kwargs):
#     print(kwargs)
#
# dict_pack_unpack(name="shola", age = 34, sex= "Male")

# def dict_pack_unpack(*args, **kwargs):
#     print("kwargs", kwargs)
#     print("Args", args)
# dict_pack_unpack(4, 5, "goal", name="shola", age=34, sex="Male")


for i in range(1, 10, 2):
    print(i, end=" ")

print()

for i in range(100, 1, -10):
    print(i, end=" ")
print()

a = "Hello World"
print(a[0:11:2])
print(a[::-1])

my_str = "hi mom"
new_str = my_str[:]
print(my_str[::-1])

b = "Wale"
for i in b:
    print(i, " ",type(i))

print(len(b))


for i in range(11,0,-1):
    print('x '*i)

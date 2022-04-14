import math

number = int(input("Enter any number: "))
number_squared = number * number
a = math.ceil(math.log10(number))
power = int(math.pow(10, a))
print(a)
print(number_squared)
print(power)

if number == (number_squared % power):
    print("it is an ambigram")
else:
    print("It is not an ambigram")

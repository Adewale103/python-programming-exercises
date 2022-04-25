n = 1
largest = 0
second_largest = 0
print("Enter number ten times")
while n <= 10:
    number = int(input("Enter number: "))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number
    n += 1
print("The largest number is ", largest)
print("The second largest number is ", second_largest)




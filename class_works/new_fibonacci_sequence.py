number = int(input("Enter any number to generate the fibonacci series: "))
a, b = 0, 1
count = 1
while count <= number:
    print(a, end=" ")
    a, b = b, a+b
    count += 1



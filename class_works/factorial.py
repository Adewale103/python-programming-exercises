number = int(input("Enter the number: "))
i = 1
fact = 1
count = 0
while i <= number:
    result = i - count
    fact = fact * result
    i += 1
print("The factorial of", number, "is", fact)

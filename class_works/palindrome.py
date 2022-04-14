number = str(input("Enter any digit: "))
if number == number[::-1]:
    print("The number is a palindrome ")
else:
    print("The number is not a palindrome")

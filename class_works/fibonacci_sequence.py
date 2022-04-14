number = int(input("Enter any number to generate the fibonacci series: "))
count = 1
previous_number = 0
next_number = 1
while count <= number:
    print(previous_number, end=" ")
    sum_ = previous_number + next_number
    previous_number = next_number
    next_number = sum_
    count += 1


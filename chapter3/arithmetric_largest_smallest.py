print("input five integers, press enter after each entry! ")
first_number = int(input("Enter Number: "))
count = 1
sum_ = first_number
product = first_number
largest = first_number
smallest = first_number
while count <= 4:
    number = int(input("Enter Number: "))
    sum_ = sum_ + number
    product = product * number
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    count += 1
average = (sum_ * 1.0)/5

print(f'The largest of the numbers is {largest}')
print(f'The smallest of the numbers is {smallest}')
print(f'The product of the numbers is {product}')
print(f'The sum of the numbers is {sum_}')
print(f'The average of the numbers is {average}')

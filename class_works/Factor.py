number = int(input("Enter a number: "))
factor = 1
sum_of_factors = 0
count = 0
while factor < number:
    if number % factor == 0:
        print(factor, " is a factor ", number)
        sum_of_factors = sum_of_factors + factor
        count += 1
    factor += 1
print(sum_of_factors)
if sum_of_factors > number:
    print("it is an abundant number")
elif sum_of_factors == number:
    print("it is a perfect number ")
elif sum_of_factors < number:
    print("it is a deficient number")






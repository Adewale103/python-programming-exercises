number = int(input("Enter any number: "))
sum_ = 0
count = number
initial = 0
while count >= 1:
    result = count - initial
    sum_ = sum_ + count
    count -= 1
print(sum_)

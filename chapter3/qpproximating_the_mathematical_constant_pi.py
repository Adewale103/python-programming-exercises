number = 4
n = 1
pi = 0
y = int(input("Enter the number of terms: "))
for i in range(1, y+1, 2):
    pi = pi + (number/i)
    print(pi)
for i in range(3, y+2, 2):
    pi = pi - (number/i)
    print(pi)




count = 1
while count != 100000:
    number = int(input("Guess a number between 1 and 10: "))
    if number == 8:
        print("You got it right")
        break
    elif number > 8:
        print("too high")
    elif number < 8:
        print("too low")
    count += 1

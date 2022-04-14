count = 1
while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print(count, "->", "fizbuzz")
    elif count % 3 == 0:
        print(count, "->", "fizz")
    elif count % 5 == 0:
        print(count, "->", "buzz")
    else:
        print(count, "->", count)
    count += 1


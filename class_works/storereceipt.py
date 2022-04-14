shape = '='
shape2 = '-'
message = 'Florence & Sons Group of Company'
message1 = '312 Herbert Marculay Way, Sabo, Yaba, Lagos, Nigeria'
message2 = '07014014012 flomarket@gmail.com'
product = []
qty_ = []
price_ = []
total_ = []
count = 0

status = True
while status:
    product_name = str(input("Enter the product you want to purchase: "))
    product.append(product_name)

    qty = int(input("Enter quantity: "))
    qty_.append(qty)

    price = int(input("Enter price: "))
    price_.append(price)

    total = qty * price
    total_.append(total)
    count += 1
    print("Do you want to buy more items?")
    response = int(input("""Enter
                        1.-> Yes
                        2.-> No
                        """))
    if response == 1:
        status = True
    elif response == 2:
        status = False

grand_total = sum(total_)

final_message = "THANKS FOR YOUR PATRONAGE!!!"

print(shape * 70)
print(' ' * 17 + message)
print('         ' + message1)
print('                 ' + message2)
print(shape * 70)
print("                product     Qty      Price     Total")
for i in range(0, count):
    print(f'{product[i]:>22}    {qty_[i]:>4}   {price_[i]:>8}   {total_[i]:>7}')
print(shape2 * 70)
print(' '*37, 'Total:   ', grand_total)
print(shape * 70)
print(' '*19 + final_message)




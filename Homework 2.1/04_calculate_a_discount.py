price = float(input("Enter the price: "))
discount = float(input("Enter the discount (%): "))

new_price = price - (price * discount / 100)

print("The new price is ", new_price)
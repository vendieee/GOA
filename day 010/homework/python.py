#first

age = int(input("how old are you?"))

if age >= 18:
    print("you can drive a car.")
else:
    print("you cant drive a car.")


#second

temp = int(input("whats the temperature outside?"))

if temp <= 16:
    print("its a cold outside.")
elif temp <= 25:
    print("its warm outside.")
elif temp >= 26:
    print("its hot outside.")    

#third

current_bread = int(input("how much bread do you have?"))
needed_bread = int(input("how much bread do you need?"))

if current_bread < needed_bread:
    print("you need to buy more bread.")
elif current_bread >= needed_bread:
    print("you have enough bread.")

#fourth

balance = float(input("Enter your balance: "))
price = float(input("Enter the item price: "))
discount_percent = float(input("Enter discount (%): "))


discount_price = price - (price * discount_percent / 100)
print("Discounted price:", discount_price, "GEL")


if balance >= discount_price:
    print("You can buy the item.")
else:
    print("You don't have enough money.")

#fifth

number = int(input("Enter a number: "))

odd = (number % 2 != 0)
single_digit = (-9 <= number <= 9)

if odd and single_digit:
    print("The number is odd and single-digit.")
elif odd:
    print("The number is odd but not single-digit.")
elif single_digit:
    print("The number is single-digit but not odd.")
else:
    print("The number is neither odd nor single-digit.")


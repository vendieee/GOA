#first

num1 = input("insert first number: 32")
num2 = input("insert second number: 8")
num3 = input("insert third number: 6.5")


num1 = 32
num2 = 8
num3 = 6.5

plus = num1 + num2
print(plus)

minus = num1 - num2
print(minus)

mul = num1 * num3
print(mul)

mul2 = num1 ** num3
print(mul2)


div = num1 / num2
print(div)

div2 = num1 // num3
print(div2)

rem = num1 % num2
print(rem)

#second

if 3 > 5:
    print("yes")
else: 
    print("no")


#third

number1 = 67

if number1 <= 100 and number1 >= 90:
    print("შესანიშნავი!")
if number1 <= 89 and number1 >= 80:
    print("კარგი!")
if number1 <= 79 and number1 >= 70:
    print("საშუალო")
if number1 <= 69 and number1 >= 60:
    print("ცუდი")
if number1 <= 59 and number1 >= 0:
    print("ძალიან ცუდი")

#fourth

age = input("შეიყვანე ასაკი: 21")

age = 19

if age >= 21:
    print("შეგიძლია ატარო ზილი ან იკარუსი.")
else:
    print("არ შეგიძლია ატარო ზილი ან იკარუსი.")

#fifth

temp = input("todays temperature is 30")
temp2 = input("todays temperature is 11")
temp = 30
temp2 = 11
weather = input("todays weather is sunny")
weather2 = input("todays weather is cloudy")
weather = "sunny"
weather2 = "cloudy"


if temp > 25 and weather == "sunny":
    print("მოკლე შარვალი და მაისური")

if temp < 10 or weather == "rainy":
    print("ქურთუკი და ქოლგა")
else:
    print("ჩვეულებრივი ტანსაცმელი")

#first
#for loop ტერმინალში გამოაქვს სიტყვას ან რიცხვს და ამეორებს

#second
numb=input("insert a number:")
if int(numb) > 0:
    print(numb, "დადებითია")
elif int(numb) < 0:
    print(numb, "უარყოფითი")
else:
    print(numb, "არც ერთია")

#third
numb2=input("insert a number:")
if int(numb2) % 2 == 0:
    print(numb2, "არის ლუწი")
else:
    print(numb2, "არის კენტი")

#fourth
exam=input("what score did you get?")
if int(exam) >= 50:
    print("მალადეც")
else:
    print("ვერ ჩააბარე")

#fifth
number1=input("insert the first number:")
number2=input("insert the second number:")
if (int(number1) + int(number2)) % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")
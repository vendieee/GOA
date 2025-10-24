# 1) ლუწი თუ კენტი
def check_even_odd():
    num = int(input("შეიყვანე რიცხვი: "))
    if num % 2 == 0:
        print("ეს რიცხვი ლუწია.")
    else:
        print("ეს რიცხვი კენტია.")


# 2) დადებითი თუ უარყოფითი
def check_positive_negative():
    num = int(input("შეიყვანე რიცხვი: "))
    if num > 0:
        print("ეს რიცხვი დადებითია.")
    elif num < 0:
        print("ეს რიცხვი უარყოფითია.")
    else:
        print("ეს ნულია.")


# 3) შედარება
def compare_numbers():
    a = int(input("შეიყვანე პირველი რიცხვი: "))
    b = int(input("შეიყვანე მეორე რიცხვი: "))
    if a > b:
        print(a, "უფრო დიდია ვიდრე", b)
    elif a < b:
        print(b, "უფრო დიდია ვიდრე", a)
    else:
        print("ორივე რიცხვი ტოლია.")


# 4) ქულა
def grade_system():
    score = int(input("შეიყვანე ქულა (0-100): "))
    if 90 <= score <= 100:
        print("შენი ნიშანია: A")
    elif 80 <= score <= 89:
        print("შენი ნიშანია: B")
    elif 70 <= score <= 79:
        print("შენი ნიშანია: C")
    elif 60 <= score <= 69:
        print("შენი ნიშანია: D")
    elif 0 <= score <= 59:
        print("შენი ნიშანია: F")
    else:
        print("შეიყვანე სწორი ქულა 0-დან 100-მდე!")


# 5) ტემპერატურა
def check_temperature():
    temp = float(input("შეიყვანე ტემპერატურა ცელსიუსში: "))
    if temp < 0:
        print("Today is very cold! Wear warm clothes 💙")
    elif 0 <= temp <= 30:
        print("Today is a really nice weather 🥰")
    else:
        print("Today is very hot! Drink plenty of water 🔥")

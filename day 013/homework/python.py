# 1) for loop Python-ში გამოიყენება, რათა განმეორებით შესრულდეს კოდი სიაში ან რიცხვებში.


# 2) დადებითია თუ უარყოფითი
num = float(input("შეიყვანე რიცხვი (დადებითი/უარყოფითი): "))
if num > 0:
    print("რიცხვი დადებითია")
elif num < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი ნულია")

print()

# 3) კენტი თუ ლუწი
num = int(input("შეიყვანე რიცხვი (კენტი/ლუწი): "))
if num % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")

print()

# 4) ქულა
score = int(input("შეიყვანე ქულა (0-100): "))
if score == 100:
    print("მალადეც!")
elif score < 50:
    print("ვერ ჩააბარე")
else:
    print("ნორმალური შედეგი")

print()

# 5)
num = int(input("შეიყვანე რიცხვი დამატებისთვის: "))
my_number = 5  
total = num + my_number
if total % 2 == 0:
    print("ჯამის შედეგი ლუწია:", total)
else:
    print("ჯამის შედეგი კენტია:", total)

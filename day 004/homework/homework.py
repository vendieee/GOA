#first 
# "+" შეკრების ოპერატორი
# იყენება ორი რიცხვის დასამატებლად
# მაგ. x = 5 + 3  შედეგი: 8

# "-" გამოკლების ოპერატორი
# აკლებს მეორე რიცხვს პირველს
# მაგ. x = 10 - 4   შედეგი: 6

# "*" გამრავლების ოპერატორი
# ამრავლებს ორ რიცხვს ერთმანეთზე
# მაგ. x = 6 * 7  შედეგი: 42

# "/" გაყოფის ოპერატორი
# აკეთებს წილადობრივ გაყოფას 
# მაგ. x = 15 / 2   შედეგი: 7.5

# "//" მთელი გაყოფის ოპერატორი
# გაყოფს და აბრუნებს მხოლოდ მთლიან ნაწილს
# მაგ. x = 15 // 2   შედეგი: 7

# % ნაშთის ოპერატორი
# გვაჩვენებს გაყოფის ნაშთს
# მაგ. x = 15 % 2   შედეგი: 1

# ** ხარისხის ოპერატორი
# აყავს რიცხვი ხარისხში
# მაგ. x = 2 ** 3   შედეგი: 8 (2 * 2 * 2)


#second

number1 = input("შეიყვანე პირველი რიცხვი: 3")
number2 = input("შეიყვანე მეორე რიცხვი: 6")

number1 = 3
number2 = 6

# ვკრიბავთ ორ რიცხვს
bla = number1 + number2

# ვბეჭდავთ შედეგს
print("ორი რიცხვის ჯამი არის:", bla)


#third

a = 10
b = 3

# შეკრება
plus_result = a + b 
print("შეკრება:", plus_result)

# გამოკლება
minus_result = a - b 
print("გამოკლება:", minus_result)

# გამრავლება
multi_result = a * b 
print("გამრავლება:", multi_result)

# გაყოფა 
divide_result = a / b  
print("გაყოფა:", divide_result)

# მთელი გაყოფა
divide2_result = a // b 
print("მთელი გაყოფა:", divide2_result)

# ნაშთი
idk_result = a % b 
print("ნაშთი:", idk_result)

# ხარისხში აყვანა
vol_result = a ** b 
print("ხარისხში აყვანა:", vol_result)


#fourth

balls = 4
boxes = 3

total_balls = balls * boxes

print("სულ ბურთების რაოდენობა არის:", total_balls)


#fifth

my_age = 14
mom_age = 44
dad_age = 50
sister_age = 21

print("მე ნაკლები ასაკის ვარ მამაზე?", my_age < dad_age)  # True

print("დედა მეტია დასზე?", mom_age > sister_age)  # True

print("დედა >= მამა?", mom_age >= dad_age)  # False

print("და <= მე?", sister_age <= my_age)  # True

print("მე და და ტოლი ასაკის ვართ?", my_age == sister_age)  # False

print("მამა != დედა?", dad_age != mom_age)  # True






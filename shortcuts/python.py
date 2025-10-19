# ცვლადი ინახავს მნიშვნელობას
# heiehi --->  variable / ცვლადი
#   =    ----> ინახავს 
# "პიპი" ---> პიპი

# heihi ---> name  / სახელი
# "პიპი" --> value / მინიშნვნელობა
heihei = "პიპი"

print(heihei)

# მონაცემთა ტიპები / data type
# ტექსტური მონაცემები / text data --- 1    -> string  ""❣️  /  ''❣️       "'💔   ---> "pipi" 
# ციფრული მონაცემები / numeric data --- 3  -> integer / მთელი 1,3,4,5,6   float / ათწილადი -> 1.3 , 1.4, 14.68   imaganary number 3+5j

#----------------------------------------------------------------------------------
# ტექსტურ მონაცემებს არ ემატებათ + ციფრული მონაცემები 💔
x = 1 
y = "ლომი"
# print(x + y)
# ყველა ფუნცქიას ბოლოში აქვს ( ) გამხსნელი და დამხურავი ფრჩილები
# python და ზოგადად პროგრამირებაში გვაქვს ჩშენებული -----> შექმნილი ფუნციები 
# მაგ: print(), str(), int(), float(), type()

# str() ------> ფუნქციის ( ვგულისხმობ გამხსნელი  --> ( <-- და დამხურავი --> ) <--- ფრჩილების შიგნით  ) ) შიგნით რასაც დავწეᲠᲗ
# ᲧᲕᲔᲚᲐᲤᲔᲠᲘ ᲒᲐᲓᲐᲘᲥᲪᲔᲕᲐ stringn ად 


print( type( 1 ) )
print( type( 1.5 ) )
print( type( "lomi" ) )
# concatination  / კონკატინაცია ნიშნავს string ების შეერთებას
x = 18
name = "ლომი"

print(name + "არის" + str( x ) + "წლის")





name = "davit"
age = 21

# ცვლადის შემქმნის დროს არ შეიძლება რომ გამოვიყენოთ სომბლოები !, &, #, არ შეიძლება რომ ამით დაიწყოს
# არ შეიძება რომ ციფრით
group = 3  
_gio = ""

salome = 4

print("solomoni 55 wlis aris")







# ეს ცვლადი ინახავს ჩემი სახელის მნიშვნელობას
name = "davit" # <-- ბრჭყალებში მოთავსებული მნიშნველობა ყოველთვის არის string

"""

"""
# --------------------------------------------------------------------------------
#         input არის ფუნქცია რომლის შიგნით () იწერება               კითხვები string ის  საით
#                                                               👆
#         ჩვენ როცა გავუშვებთ კოდს terminal ში გამოვა ჩვენი დაწერილი კითხვა და როცა პასუხს გავცემთ
#         ანუ ტერმინალში დავწერთ პასუხს  inputExample ეს ცვლადი შეინახავს ჩვენს მიერ დაწერილ პასუხს 
inputExample = input("ვაშლი კაია?: ")
# user--- მომხმარებლები 
# მომხამრებელს შეეკითხეთ რამდენი ვაშლია ყთში

print(inputExample)









# Varible store value 
# Data Types: Numbers, String
# string: "" 
# Number: integer, float ---- int --> 1, 2, 3, 4 float---- 1.234 , 123.4412
# Variable can be updated
# name = "davit"
# name = 132
# print --> 132
##########################################################
# snake case-ს ვიყენებთ python -ში 
name_and_sruname = ""
##########################################################
# Maht Operators
# +
# -
# // , /
# *
# **
# %
plus = 43 + 1 + 1 + 1
minus = 43 - 1 - 1 - 1
divide_1 = 43 / 1 / 1 / 1
divide_2 = 43 // 1 // 1 // 1
mutify = 2 * 2
print("plus", plus)
print("minus", minus)
print("divide 1", divide_1)
print("divide 1", divide_2)
print("mutify", mutify)
# / VS //
# / --- // 
# / ---- გამოაქვს შედეგი float 
# // ---- გამოაქვს შედეგი int
print("----------/-Vs-//-------------")
print(13 / 2) # Float 6.5
# // გამიტანს ყოველთვის მთელ რიცხვს
print(13 // 2) # Integer (int) 6
###########################################
print("----------axarisxeba-------------")
axarisxeba = 3 ** 4
print("axarusxeba",axarisxeba)
# 2 * 2 * 2 * 2
#   4   *   4
#       16 
###########################################
print("----------nashti-%-------------")
# ციფრი თუ ზუსტად იყოფა მეორე ციფრეზე და ნაშთი გვაქვს 0 ესეიგი ეს ციფრი იყოფა მ ციფრზე უნაშთოდ
nashti = 20 % 3
# 20 % 3 არ იყოფა მაგრამ იყოფა 20 მდე 18 უახლოესი?
###########
# 20
# -
# 18
# --------
# 2
print(nashti)
###################################################################
# გამოვიყენოთ რომლიღაც მათემატიკური ოპერატორი                 #
# რომ გავარკვიოთ ჩვენი ციფრი არის თუ არა კენტი, ან ლუწი        #
######################################################################
# მე დავალებას ვწერ რომ გამოვარკიო ეს ცფირი არუის თუ არა ლუწი    #
# Bollean ტიპის ცვლადით უნდა გვიგდებდეს არის თუ არა True ან False #
#####################################################################








####################
## Math operators ##
####################
# +, -, //, /, *, **, %

###########################
## Comperation operators ##
###########################
# <, >, >=, <=, ==, !=

number = 21
isEven = "Is nmber even? "+ str(number % 2 == 0)
isOdd = "Is nmber odd? "+ str(number % 2 == 1)
print(isEven)
print(isOdd)






# if else
if 3 < 2 : # if ის შემთხევაში ყოველთვის უდნა იყოს Conditon True
    print("ME VAR LOMI")
else: # esle  False ის შემთხვევაში გამოიდს
    print("ME MAINC LOMI VAR!")







"""
*********************
*********************
*********************
*********************
"""

value = 10



print("First")
if 3 > 5: #False
    print("Second")
    print(20 * "*")
    print(20 * "*")
elif 10 < 5: #False
    print("this condition is true 1")
elif 3 < 5: #True
    print("this condition is true 2")
else: # False
    print("ლომი")
print("Third")












"""
VERSION 1 

       *
      **   
     ****
    ******
   ********
  **********
"""
print(8 * " " + "*")
print(7 * " " + 3 * "*")
print(6 * " " + 5 * "*")
print(5 * " " + 7 * "*")
print(4 * " " + 9 * "*")
print(3 * " " + 11 * "*")
print(2 * " " + 13 * "*")
print(1 * " " + 15 * "*")

"""
VERSION 2
            *
          ***
        *****
      *******
    *********
"""
print("*" * 1)
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)
print("*" * 6)
print("*" * 7)
print("*" * 8)
"""
 EASY LEVEL 
*********************
*********************
*********************
*********************
"""








for i in range(1000):  # loop 
    print("lomi")



# range(start, end, step) / range(დასაწყისი, დასასრული, ნაბიჯი)
for i in range(0, 20, 5): # 5
    print(i)     




i = 0 # 3
while i < 3:
    print("lomi")
    i = i + 1   










#    index  0          1       2           3       4        5   
fruits = ["Apple", "Samsung", "Xiaomi", "lomi", "Ak-47", "RPG-7", ] 
item3 = fruits[2]






print("-------------------------------[slice]----------------------------------")

# slice        0  1  2  3  4  5  6  7  8  9
slice_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]
#             [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]  - reversed array


# -1 last element
# -2 before last element
# -3 3rd from last element
print(array[-1])
# [start:end:step]
print(slice_array[0:5])
print(slice_array[5:]) # from index 2 to the end
print(slice_array[:8]) # from star to index 8
print(slice_array[::]) # from start to end
print(slice_array[::5]) # each 2nd element
print(slice_array[0:8:2])
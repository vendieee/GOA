# 1) lion() 
def lion():
    arr = ["apple", "banana", "cherry", "date", "fig"]
    print("Index of 'cherry':", arr.index("cherry"))

# 2) lion2() 
def lion2():
    arr = [1,1,1,1,1,1,1,2]
    last_element = arr[-1]
    print("Index of last element:", arr.index(last_element))

# 3) lion3() 
def lion3():
    name = input("შეიყვანე შენი სახელი: ")
    print(name + " მე ვარ ლომი")  


# 4) lion4() 
def lion4():
    arr = []
    for i in range(1, 21):  
        if i % 2 != 0:
            arr.append(i)
    print("Odd numbers:", arr)

# 5) lion5() 
def lion5():
    password = "1234"  
    user_input = ""
    while user_input != password:
        user_input = input("შეიყვანე პაროლი: ")
        if user_input != password:
            print("პაროლი არასწორია")
    print("გაუმარჯოს, პაროლი სწორია")

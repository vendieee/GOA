# 6) array ნიშნავს მონაცემთა სიას (list)
# def გამოიყენება ფუნქციის შესაქმნელად Python-ში


# 1) lion() 
def lion():
    animals = ["dog", "cat", "lion", "tiger", "bear"]
    print(animals.index("lion"))  


# 2) lion2() 
def lion2():
    nums = [1, 1, 1, 1, 1, 1, 1, 2]
    last_index = nums.index(2)  
    print(nums[last_index])     


# 3) lion3() 
def lion3(name):
    print(name, "მე ვარ ანანო ლომი <3")


# 4) lion4() 
def lion4():
    odd_numbers = []
    for i in range(1, 11):
        if i % 2 != 0:
            odd_numbers.append(i)
    print(odd_numbers)


# 5) lion5() 
def lion5():
    password = "lion123"
    guess = ""
    while guess != password:
        guess = input("შეიყვანე პაროლი: ")
        if guess != password:
            print("პაროლი არასწორია!")
    print("პაროლი სწორია!")


# 7) 
data = ["apple", "banana", "apple", "orange", "apple"]
print(data.count("apple"))  # რამდენჯერაა "apple"


# 8) 
def multiply(a, b):
    print(a * b)


# 9) 
def lion6():
    animals = ["Lion", "Tiger", "Frog", "Panda", "Deer", "Elephant", "Fox"]
    print(animals[1], animals[2])    
    print(animals[-6], animals[-5])  


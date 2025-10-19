#first
names = ["ნინო", "გიორგი"]  
names.append("ანდრია")       
print(names)

# second
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

# third
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "nectarine"]

for word in words[1::2]:
    print(word)

# fourth
word = "academy"
i = 1

for letter in word:
    print(letter + "-" + str(i))
    i += 1

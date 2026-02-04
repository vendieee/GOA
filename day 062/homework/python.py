# 1)
# tuple არის მონაცემთა ტიპი, რომელიც ინახავს რამდენიმე ელემენტს
# tuple-ის მთავარი განსხვავება list-სგან ისაა, რომ tuple არის უცვლელი
# list-ის შეცვლა შეიძლება, tuple-ის არა

# 2) tuple 3 ელემენტით: სახელი, ასაკი, ქალაქი
person = ("Andria", 14, "Tbilisi") #about to be 15 in 7th feb :DDDDDDDDDDDDDDDDDD

# 3) tuple-ის პირველი ელემენტის გამოტანა
print(person[0])

# 4) tuple-ის ელემენტის შეცვლა
person[1] = 15   # ეს გამოიწვევს ერორს

# 5) tuple 5 რიცხვით
numbers = (1, 2, 3, 4, 5)
print(len(numbers))

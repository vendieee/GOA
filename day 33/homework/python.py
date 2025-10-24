# 1) "default value" ნიშნავს ნაგულისხმევ მნიშვნელობას, 
# ანუ როცა ფუნქციას არგუმენტი არ გადაეცემა, ის ავტომატურად ამ მნიშვნელობას გამოიყენებს.


# 2) return აბრუნებს მნიშვნელობას ფუნქციიდან



# 3) სხვაობა
def substract(a, b):
    return a - b


# 4) გამრავლება
def multiply(a, b):
    return a * b


# 5) გაყოფა
def divide(a, b):
    return a / b


# მაგალითები:
print(substract(10, 4))   # 6
print(multiply(3, 5))     # 15
print(divide(20, 4))      # 5.0

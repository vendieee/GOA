#1

def make_repeater(n):
    def repeat(text):
        return text * n
    return repeat


#2


def bank_account(initial_balance):
    balance = initial_balance

    def withdraw(amount):
        nonlocal balance
        balance -= amount
        print(balance)

    return withdraw



#3


def power_of(base):
    def power(exponent):
        return base ** exponent
    return power


#4


points = 10

def add_point():
    global points
    points += 1
    print(points)

add_point()


#5


def calculate_rectangle_area(a, b):
    return a * b


#6


logs = []

def add_log(message):
    logs.append(message)



#7


def calculate_tax(tax_rate):
    def tax(price):
        return price * tax_rate
    return tax

georgian_tax = calculate_tax(0.18)

print(georgian_tax(100))
print(georgian_tax(250))



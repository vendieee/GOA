# 1)
def apply_op(a, b, func):
    return func(a, b)



# 2)
def make_greeter(greeting):
    def greeter(name):
        print(greeting + " " + name)
    return greeter

# 3)
def my_filter(lst, predicate):
    result = []
    for item in lst:
        if predicate(item):
            result.append(item)
    return result


# 4)
def process_string(text, action):
    return action(text)


# 5)
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def double(x):
    return x * 2

functions = [square, cube, double]

x = 5
for f in functions:
    print(f(x))


# 6)
def safe_execute(func, x):
    try:
        result = func(x)
        print("Success")
        return result
    except:
        print("Error")


# 7)
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply


# 8)
def my_map(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result


# 9)
def run_if_positive(func, value):
    if value > 0:
        return func(value)


# 10)
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed
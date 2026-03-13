# 1)
def safe_execute(func, x):
    try:
        result = func(x)
        print("Success")
        return result
    except:
        print("Error")


# 2)
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply


# 3)
def my_map(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result


# 4)
def run_if_positive(func, value):
    if value > 0:
        return func(value)


# 5)
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed
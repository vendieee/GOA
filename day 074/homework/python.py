#1

def apply_operation(numbers, operation):
    result = []
    for x in numbers:
        result.append(operation(x))
    return result


#2

def my_map(func, lst):
    result = []
    for x in lst:
        result.append(func(x))
    return result


#3

def my_filter(func, lst):
    result = []
    for x in lst:
        if func(x):
            result.append(x)
    return result


#4

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply


#5

def repeat(func, n):
    def new_func():
        for _ in range(n):
            func()
    return new_func
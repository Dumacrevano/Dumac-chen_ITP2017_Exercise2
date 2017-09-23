
def fib(x):

    result=[0]
    a=1
    b=1
    while a < x:
        result.append(a)
        y = b
        b = a + b
        a = y
    return result
print(fib(10))



def fib(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b


fibs=fib(5)
for i in range (5):
    print(fibs.__next__())
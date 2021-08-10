def fact(n):
    for i in range (n-1):
        n=n*(n-1)
        n=n-1
    print (n)

fact(5)
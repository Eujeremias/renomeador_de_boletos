def some_ateh(n):
    if(n==0):
        return 0
    else:
        return n + some_ateh(n - (n - 1))

print(some_ateh(5))
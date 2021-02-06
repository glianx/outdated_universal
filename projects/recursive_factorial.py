from icecream import ic
def factorial(n):
    if n <= 1:
        ic(n)
        return 1
    else:
        x = factorial(n-1)
        ic(n,x,n*x)
        return n * x
print(factorial(5))
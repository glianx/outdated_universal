from icecream import ic
def factorial(n):
    if n <= 1:
        ic(n)
        return 1
    else:
        ic(n)
        return n * factorial(n-1)
print(factorial(5))
def mobile_points(n):
    if n == 0:
        return 4
    return mobile_points(n-1) * .75 + 4

for i in range(100):
    print(mobile_points(i))
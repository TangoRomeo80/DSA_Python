def swapWithoutTemp(x, y):
    x = x + y
    y = x - y
    x = x - y

    return x, y

print(swapWithoutTemp(10, 15))
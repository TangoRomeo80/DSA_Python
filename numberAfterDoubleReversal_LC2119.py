def isSameAfterReversals(num):
    if (num  % 10 == 0 and num != 0):
        return False
    return True

print(isSameAfterReversals(1800))
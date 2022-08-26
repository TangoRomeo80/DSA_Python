from collections import Counter


def reorderedPowerOf2(n):
    c = Counter(str(n))
    for i in range(30):
        if c == Counter(str(2 ** i)):
            return True
    return False
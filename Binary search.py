# the following lines are reserved for imports
#
#

def binary_search(data, key, l, r):
    if l > r:
        return False
    else:
        m = (l + r) // 2
        if key == data[m]:
            return True
        elif key < data[m]:
            return binary_search(data, key, l, m - 1)
        else:
            return binary_search(data, key, m + 1, r)


# driver code
if __name__ == '__main__':
    arr = [6, 7, 8, 9, 10, 11, 3, 6, 7, 4, 7, 5, 6, 124, 23, 1324, 234]
    arr.sort()
    print(binary_search(arr, 8, 0, len(arr) - 1))

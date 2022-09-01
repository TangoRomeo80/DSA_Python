def removeDuplicates(arr):
    d = {i:0 for i in arr}

    res = []

    for i in arr:
        if d[i] == 0:
            res.append(i)
        d[i] = 1

    return res

print(removeDuplicates([ 1, 2, 5, 1, 7, 2, 4, 2 ]))
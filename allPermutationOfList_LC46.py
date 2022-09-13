def permutation(lst):
    if not lst:
        return []
    
    if len(lst) == 1:
        return [lst]
    
    res = []

    for i in range(len(lst)):
        for p in permutation(lst[:i] + lst[i+1:]):
            res.append([lst[i]] + p)

    return res

print(permutation([1, 2, 3])) 
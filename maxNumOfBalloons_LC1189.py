def maxNumberOfBalloons(text):
    d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
    for c in text:
        if c in d:
            d[c] += 1
    return min(d['b'], d['a'], d['l'] // 2, d['o'] // 2, d['n'])
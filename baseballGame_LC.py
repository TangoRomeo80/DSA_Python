def calPoints(ops):
    score = []
    for i in ops:
        if i == 'C':
            score.pop()
        elif i == 'D':
            score.append(2*score[-1])
        elif i == '+':
            score.append(score[-1]+score[-2])
        else:
            score.append(int(i))
    return sum(score)
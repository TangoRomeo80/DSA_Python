import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
inputs = []

for i in range(n):
    line = input()
    new = []
    for l in line:
        new.append(l)
    inputs.append(new)

max_len = len(max(inputs, key=len))
lines = []

for i in range(n + 2):
    new = []
    for j in range(max_len + 2):
        new.append(' ')
    lines.append(new)

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        lines[i][j] = inputs[i][j]

canvas = []

for i in range(n + 2):
    new = []
    for j in range(max_len + 2):
        new.append(' ')
    canvas.append(new)

for i in range(n):
    for j in range(len(lines[i])):
        if (lines[i][j] != ' ' and canvas[i][j] == ' ') or (lines[i][j] != ' ' and ((canvas[i][j] == '`') or (canvas[i][j] == '-'))):
            canvas[i][j] = lines[i][j]
            if lines[i + 1][j + 1] == ' ':
                canvas[i + 1][j + 1] = '-'
                if lines[i + 1][j + 1] == ' ':
                    canvas[i + 2][j + 2] = '`'
        elif canvas[i][j] == ' ':
            canvas[i][j] = lines[i][j]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for line in canvas:
    print(''.join(line).rstrip())

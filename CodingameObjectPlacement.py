def read_input():
    row, col = [int(x) for x in input().split()]
    arr = [list(input()) for _ in range(row)]
    return arr


def print_output(obj):
    for i in obj:
        print(''.join(i))


def test_pos(obj, grid, row, col):
    for i in range(len(obj)):
        for j in range(len(obj[0])):
            if grid[row + i][col + j] != '.' and obj[i][j] != '.':
                return False
    return True


def place_at_pos(obj, grid, row, col):
    arr = grid
    for i in range(len(obj)):
        for j in range(len(obj[0])):
            if obj[i][j] != '.':
                arr[row + i][col + j] = obj[i][j]
    return arr


ob = read_input()
gr = read_input()

positions = []

for di in range(len(gr) - len(ob) + 1):
    for dj in range(len(gr[0]) - len(ob[0]) + 1):
        if test_pos(ob, gr, di, dj):
            positions.append((di, dj))

print(len(positions))

if len(positions) == 1:
    display = place_at_pos(ob, gr, positions[0][0], positions[0][1])
    print_output(display)

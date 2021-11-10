def get_inversion(arr, n):
    count = 0
    for i in range((n ** 2) - 1):
        for j in range(i + 1, n ** 2):
            if (arr[i] != 0) and (arr[j] != 0) and (arr[i] > arr[j]):
                count += 1

    return count


def check_blank_position(arr, n):
    for i in range((n - 1), -1, -1):
        for j in range((n - 1), -1, -1):
            if arr[i][j] == 0:
                return n - i


def is_solvable(arr, n):
    inversion = get_inversion([j for sub in arr for j in sub], n)
    if (n % 2) != 0:
        return (inversion % 2) == 0

    else:
        pos = check_blank_position(arr, n)
        if (pos % 2) != 0:
            return (inversion % 2) == 0
        else:
            return (inversion % 2) != 0


puzzle = []
num_of_rows = int(input('Enter number of rows: '))
print('Enter the puzzle in sequence: ')
for i in range(num_of_rows):
    puzzle.append([int(x) for x in input().split()])

if is_solvable(puzzle, num_of_rows):
    print('Solvable')
else:
    print('Not solvable')

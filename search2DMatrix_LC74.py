def searchMatrix(matrix, target):
    # if not matrix:
    #     return False
    # row = 0
    # col = len(matrix[0]) - 1
    # while row < len(matrix) and col >= 0:
    #     print(row, col)
    #     if matrix[row][col] == target:
    #         return True
    #     elif matrix[row][col] > target:
    #         col -= 1
    #     else:
    #         row += 1
    # return False

    # binary search
    if not matrix:
        return False
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        print(top, bot)
        mid = (top + bot) // 2
        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bot = mid - 1
        else:
            break

    if top > bot:
        return False

    print()

    row = (top + bot) // 2
    left, right = 0, COLS - 1
    while left <= right:
        print(left, right)
        mid = (left + right) // 2
        if target == matrix[row][mid]:
            return True
        elif target > matrix[row][mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False

searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
def isPerfectSquare(num):
    # for i in range(1, num + 1):
    #     if i * i == num:
    #         return True
    #     if i * i > num:
    #         return False

    # binary search
    left, right = 1, num

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
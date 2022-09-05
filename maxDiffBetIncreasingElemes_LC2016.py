def maximumDifference(nums):
    l, r = 0, 1
    maxDiff = -1
    while r < len(nums):
        if nums[l] < nums[r]:
            maxDiff = max(maxDiff, nums[r] - nums[l])
        else:
            l = r
        r += 1

    return maxDiff
            
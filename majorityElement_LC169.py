def majorityElement(nums):
    # nums.sort()
    # return nums[len(nums)//2]
    count = {}
    res, maxCount = 0, 0
    for n in nums:
        count[n] = 1 + count.get(n, 0)
        if count[n] > maxCount:
            res = n
            maxCount = count[n]
    return res
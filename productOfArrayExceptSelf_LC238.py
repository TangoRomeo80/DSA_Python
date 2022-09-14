def productExceptSelf(nums):
    # Time: O(n) | Space: O(n)

    # prefix = [1] * len(nums)
    # suffix = [1] * len(nums)
    # #calculate prefix array
    # for i in range(1, len(nums)):
    #     prefix[i] = prefix[i-1] * nums[i-1]
    # #calculate suffix array
    # for i in range(len(nums)-2, -1, -1):
    #     suffix[i] = suffix[i+1] * nums[i+1]
    # #calculate product of prefix and suffix
    # return [prefix[i] * suffix[i] for i in range(len(nums))]

    # Time: O(n) | Space: O(1)
    res = [1] * len(nums)
    #calculate prefix array
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    #calculate suffix array
    suffix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res


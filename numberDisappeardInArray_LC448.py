def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    
    # res = {}
    # out = []
    # for i in range(len(nums)):
    #     res[nums[i]] = 1

    # for i in range(1, len(nums) + 1):
    #     if i not in res:
    #         out.append(i)
        
    # return out



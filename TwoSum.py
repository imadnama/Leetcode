def twoSum(nums, target):
    numshash_map = {}
    for i, num in enumerate(nums):
        completionToTarget = target - num
        if completionToTarget in numshash_map:
            return [numshash_map[completionToTarget], i]
        numshash_map[num] = i
    return []


nums = [1,2,3,4,5,6,7,8,9]
print(twoSum(nums, 9))
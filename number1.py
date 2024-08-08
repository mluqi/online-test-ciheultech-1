def twosum(nums, target):

    value_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in value_index:
            return [value_index[complement], i]
        
        value_index[num] = i
    return[]

nums = [2, 7, 11, 15]
target = 9
target2 = 18
print(twosum(nums, target))
print(twosum(nums, target2))
def singlenNUmber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums1 = [2, 2, 1]
nums2 = [4,1,2,1,2]
print(singlenNUmber(nums1))
print(singlenNUmber(nums2))
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoS(nums, target):
    result = []
    res1 = -1
    for num1 in nums:
        res1 += 1
        res2 = -1
        for num2 in nums:
            res2 += 1
            if num1 + num2 == target:
                if res1 != res2:
                    result.append(res1)
                    result.append(res2)
                    print result
                    return result


twoS([2, 7, 11, 15], 9)

def twoSum(nums, target):
    result = []
    for num in nums:
        if target - num in nums:
            if nums.index(num) != nums.index(target-num):
                result.append(nums.index(num))
                result.append(nums.index(target-num))
                return result
            elif nums.index(num) == nums.index(target-num):
                pos = nums.index(num)
                while True:
                    try:
                        pos = nums.index(target-num, pos+1)
                        result.append(nums.index(num))
                        result.append(pos)
                        return result
                    except ValueError:
                        break

print twoSum([3,3], 6)

print twoSum([2,5,5,11], 10)
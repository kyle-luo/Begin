# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
#
# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
#
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for j, x in enumerate(nums1):
            i = nums2.index(x) + 1
            while i < len(nums2):
                if nums2[i] > x:
                    output.append(nums2[i])
                    break
                i += 1
            if len(output) - 1 < j:
                output.append(-1)
        return output


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check = {}
        for i, num in enumerate(nums2):
            j = i + 1
            while j < len(nums2):
                if nums2[j] > num:
                    check[num] = nums2[j]
                    break
                j += 1
            check[num] = check.get(num, -1)
        output = []
        for num in nums1:
            output.append(check[num])
        return output
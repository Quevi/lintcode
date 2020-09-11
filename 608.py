class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        i = 0
        j = len(nums) - 1
        while 0 <= i < j < len(nums):
            sum = nums[i] + nums[j]
            if sum == target:
                return i + 1, j + 1
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1

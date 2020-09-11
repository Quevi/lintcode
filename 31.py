class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        smaller = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] < k:
                nums[smaller], nums[cur] = nums[cur], nums[smaller]
                smaller += 1
                cur += 1
            else:
                cur += 1
        return smaller
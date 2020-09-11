class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        end = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] != 0:
                nums[end], nums[cur] = nums[cur], nums[end]
                end += 1
                cur += 1
            else:
                cur += 1
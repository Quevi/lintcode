class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        """
        x[左] > x[右]
        """
        # write your code here
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

print(Solution().findMin([4,3]))
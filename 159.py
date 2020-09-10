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
        if nums[0] == nums[-1]:
            res = nums[0]
            for n in nums:
                res = min(n, res)
            return res

        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])

# Solution().findMin([2,1])
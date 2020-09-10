class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    loop invariant: "区间一定包含最后那个数"
    等价于 x[left] <= target, x[right + 1] > target
    """
    def lastPosition(self, nums, target):
        # write your code here
        if nums.__len__() == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        if nums[l] != target:
            return -1
        else:
            return l

Solution().lastPosition([1,2,2,4,5,5], 5)
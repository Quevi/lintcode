class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    loop invariant: "山峰一定在区间内"
    等价于：x[left - 1] <= x[left] <= x[left + 1] and x[right - 1] >= x[right] >= x[right + 1]
    """
    def mountainSequence(self, nums):
        # write your code here
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

Solution().mountainSequence([10,9,8,7,6])
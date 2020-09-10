class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        """
        保证[l, r]一定包含target，直到r = l + 1
        """
        # write your code here
        if A[0] >= target:
            return A[:k]
        if A[-1] <= target:
            return list(reversed(A[-k:]))

        l = 0
        r = len(A) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if target < A[mid]:
                r = mid
            else:
                l = mid

        res = []
        while len(res) < k:
            if l < 0:
                res.append(A[r])
                r += 1
            elif r >= len(A):
                res.append(A[l])
                l -= 1
            elif target - A[l] <= A[r] - target:
                res.append(A[l])
                l -= 1
            else:
                res.append(A[r])
                r += 1
        return res

Solution().kClosestNumbers([1,4,6,10,20], 21, 4)
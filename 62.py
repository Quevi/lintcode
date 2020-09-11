class Solution:
    def search(self, A, target):
        lo = 0
        hi = len(A)-1
        while lo < hi:
            mid = (lo+hi) // 2
            if A[mid] > A[hi]:
                lo = mid+1
            else:
                hi = mid
        # // lo==hi is the index of the smallest value and also the number of places rotated.
        rot = lo
        lo = 0
        hi = len(A) - 1
        # // The usual binary search and accounting for rotation.
        while lo <= hi:
            mid = (lo+hi)//2
            realmid = (mid + rot) % len(A)
            if A[realmid] == target:
                return realmid
            if A[realmid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

print(Solution().search([4, 5, 1, 2, 3], 1))
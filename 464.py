class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def partition(self, A, begin, end):
        if begin == end:
            return

        pivot = A[begin]
        smaller = begin + 1
        cur = begin + 1
        while cur < end:
            if A[cur] < pivot:
                A[smaller], A[cur] = A[cur], A[smaller]
                smaller += 1
                cur += 1
            else:
                cur += 1
        A[begin], A[smaller] = A[smaller], A[begin]
        return smaller

    def quicksort(self, A, begin, end):
        # write your code here
        if len(A) == 0:
            return

        pivot = self.partition(A, 0, len(A))
        self.quicksort(A, 0, pivot)
        self.quicksort(A, pivot + 1, len(A))

    def sortIntegers2(self, A):
        # write your code here

        self.quicksort(A, 0, len(A))
class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    maxlen = 0
    left = 0

    def extend(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i, j

    def longestPalindrome(self, s):
        # write your code here
        if len(s) < 2:
            return s
        maxlen = 1
        lo = 0
        for i in range(len(s)):
            l, r = self.extend(s, i, i)
            if r - l - 1 > maxlen:
                maxlen = r - l - 1
                lo = l + 1
            l, r = self.extend(s, i, i + 1)
            if r - l - 1 > maxlen:
                maxlen = r - l - 1
                lo = l + 1
        return s[lo:(lo + maxlen)]

print(Solution().longestPalindrome('bb'))
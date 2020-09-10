class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        begin = 0
        end = len(s) - 1
        if end <= 0:
            return True

        while begin <= end:
            if not (s[begin].isalpha() or s[begin].isnumeric()):
                begin += 1
                continue

            if not (s[end].isalpha() or s[end].isnumeric()):
                end -= 1
                continue

            if s[begin] == s[end]:
                begin += 1
                end -= 1
            else:
                return False
        return True

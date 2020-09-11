class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if target == "":
            return 0

        s = 0
        t = 0
        while s < len(source):
            if source[s] == target[t]:
                s += 1
                t += 1
                if t == len(target):
                    return s - t
            else:
                s = s + 1 - t
                t = 0
        return -1

Solution().strStr("source", "target")
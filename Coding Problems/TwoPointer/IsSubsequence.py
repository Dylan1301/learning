class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j += 1
            i += 1

        if j < len(s):
            return False
        return True
    

# Check the condition before start
# Check the loop end condition
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) != (str2+str1):
            return ""
        
        a = len(str1)
        b = len(str2)

        while b > 0:
            a , b = b, a%b

        return str1[:a]
    
# Online solution suggest using Ecludian common division
# First check if the concatenation of two string are the same -> if different then return ""
# This is because if str1 = "tt" -> str2 should also be "tttt" (or t*4) -> combination of both string should be t*6
# The problem turn to using mod 
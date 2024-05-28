# My solution:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1,pointer2 = 0,0
        output = ""
        while pointer1 < len(word1) and pointer2 < len(word2):
            output += word1[pointer1] + word2[pointer2]
            pointer1 += 1
            pointer2 += 1

        if pointer1 == len(word1):
            output += word2[pointer2::]
        elif pointer2 == len(word2):
            output += word1[pointer1::] 
        
        return output


# Enhancement: May used list and append for faster operation (Does not needed to create new string every time)
# join for one string operation

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1,pointer2 = 0,0
        output = []
        len1, len2 = len(word1), len(word2)
        while pointer1 < len1 and pointer2 < len2:
            output.append(word1[pointer1])
            output.append(word2[pointer2])
            pointer1 += 1
            pointer2 += 1

        if pointer1 < len1:
            output.append(word1[pointer1::])
        elif pointer2 < len2:
            output.append(word2[pointer2::])
        
        return "".join(output)

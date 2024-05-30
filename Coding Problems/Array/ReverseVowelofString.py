# Array
# 2 pointer

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {"a", "e", "i", "o", "u", "A", "I", "U", "E", "O"}
        slist = [*s]
        i, j= 0, len(s)-1

        while i < j:
            top = slist[i]
            last = slist[j]

            if top in vowel and last not in vowel:
                j -= 1
                continue
            if last in vowel and top not in vowel:
                i +=1 
                continue
            if last in vowel and top in vowel:
                slist[i], slist[j] = last, top
            
            i +=1
            j -= 1
            
        return "".join(slist)
            
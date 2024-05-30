class Solution:
    def reverseWords(self, s: str) -> str:
        stringlist = s.split()
        i, j = 0, len(stringlist)-1

        while i < j:
            stringlist[i], stringlist[j] = stringlist[j], stringlist[i]
            i +=1
            j -=1
        return " ".join(stringlist)



#fast solution
    def reverseWords(self, s: str) -> str:
        return " ".join((s.split()[::-1]))
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        map = [0] * 101
        res = []
        count = 0

        for i in heights:
            map[i] +=1
        
        for i in range(len(map)):
            for a in range(map[i]):
                res.append(i)

        for i, v in zip(res,heights):
            if i != v:
                count+=1
        
        return count
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        map = [0] * 101
        for i in nums:
            map[i] +=1
        
        for index in range(1,len(map)):
            map[index] += map[index-1]
        
        return [x for x in range(map[target-1], map[target])]
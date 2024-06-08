
# Less efficient answer

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for i in arr:
            if i in map:
                map[i] +=1
            else:
                map[i] = 1
        
        if len(map.keys()) == len(set(map.values())):
            return True
        return False
    


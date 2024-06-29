class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # denoting importance [node number, value, ]
        # Not optimal solution
        map = {}
        res = []
        cur = 0
        for edge in roads:
            for val in edge:
                if val in map:
                    map[val] +=1
                else:
                    map[val] = 1
        
        for key, val in map.items():
            res.append([key, val])
        
        res.sort(key = lambda x: -x[1])

        for index in range(len(res)):
            map[res[index][0]] = n
            n-=1
        
        for pair in roads:
            cur += (map[pair[0]] + map[pair[1]])

        
        return cur

        



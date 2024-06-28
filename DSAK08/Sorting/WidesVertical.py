# Leetcode problem: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    points.sort(key = lambda x: x[0])
    max_val = 0
    for i in range(1,len(points)):
        max_val = max(points[i][0] - points[i-1][0], max_val)
    
    return max_val
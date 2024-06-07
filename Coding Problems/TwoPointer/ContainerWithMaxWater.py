class Solution:
    def maxArea(self, height: List[int]) -> int:
        max, i, j = 0, 0, len(height)-1
        
        while i < j:
            length = j - i
            left = height[i]
            right = height[j]

            if left <= right:
                current = left * length
                i += 1
            else:
                current = right * length
                j -= 1
            
            if current > max:
                max = current

        return max
    

# Using greedy algorithm
# Move the pointer in the direction where side is lower than the other side
# For example if side left < right => move pointer to the next left value

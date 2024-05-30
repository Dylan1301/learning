class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = 0
        for kid in candies:
            if kid > high:
                high = kid
        
        for i in range(len(candies)):
            candies[i] = ((candies[i]+extraCandies) >= high)
        
        return candies
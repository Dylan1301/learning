class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = 1000000000000000000000000,100000000000000000000
        for num in nums:
            if num <= i:
                i = num
            elif num <= j :
                j = num
            else:
                return True
        return False
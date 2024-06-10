class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left, right = 0, total
        for i in range(len(nums)):
            right = right - nums[i]

            if left == right:
                return i
            
            left += nums[i]
        
        return -1

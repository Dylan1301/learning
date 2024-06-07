class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max = 0
        current = 0
        j = 0
        for i in range(k):
            current += nums[i]
            max = current
        
        for i in range(k, len(nums)):
            current = current + nums[i] - nums[j]

            j +=1

            if current > max:
                max = current
        
        return max/k




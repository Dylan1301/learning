# Leetcode: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        positives = set()
        for n in nums:
            if n > 0:
                positives.add(n)
        return len(positives)
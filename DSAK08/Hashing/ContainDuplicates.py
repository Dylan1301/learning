class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = set()

        for i in nums:
            if i in map:
                return True
            else:
                map.add(i)
        
        return False
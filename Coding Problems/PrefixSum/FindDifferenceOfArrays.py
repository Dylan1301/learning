class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        map1, map2 = set(nums1), set(nums2)
        output = [[], []]
        
        for i in nums1:
            if i not in map2:
                output[0].append(i)
                map2.add(i)
        
        for j in nums2:
            if j not in map1:
                output[1].append(j)
                map1.add(j)

        return output
    


# Solution 2
def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        map1, map2 = set(nums1), set(nums2)
        

        return [set1-set2, set2-set1]
        

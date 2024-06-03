class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j =0,0

        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
                j +=1
            else:
                i +=1

# Using 2 pointers and loop through each element
# pointer i moving, pointer j save the first  0  => if num[i] <> 0 => change with num[j]
# j+ 1 guarantee as 0 
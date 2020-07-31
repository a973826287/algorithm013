class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         j = 0
         l = len(nums)
         for i in range(1,l):
             if nums[i] != nums[j]:
                 nums[j+1] = nums[i]
                 j += 1    
         return j+1

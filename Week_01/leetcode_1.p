#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}
        for i in range(len(nums)):
            if hashset.get(target-nums[i]) is not None :
                return [hashset.get(target-nums[i]),i]
            hashset[nums[i]]=i

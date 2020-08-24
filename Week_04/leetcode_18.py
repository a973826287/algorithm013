#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n-3):
            if nums[i] + nums[i+1]*3 > target:
                break
            if nums[i] + nums[-1]*3 < target:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n-2):
                if nums[i] + nums[j] + nums[i+1]*2 > target:
                    break
                if nums[i] + nums[j] + nums[-1]*2 < target:
                    continue
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k, z = j+1, n-1
                while k < z:
                    if nums[i] + nums[j] + nums[k] + nums[z] > target:
                        z -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[z] < target:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[z]])
                        while k < z and nums[k] == nums[k+1]:
                            k += 1
                        while k < z and nums[z] == nums[z-1]:
                            z -= 1
                        k += 1
                        z -= 1
        return res
        
# @lc code=end

#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if n < 2:
            pass
        else:
            def reverse(nums, t, s):
                while t < s:
                    nums[t], nums[s] = nums[s], nums[t]
                    t += 1
                    s -= 1
            reverse(nums, 0, n-1)
            reverse(nums, 0, k-1)
            reverse(nums, k, n-1)

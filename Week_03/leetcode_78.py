#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            subres = []
            for i in res:
                tep = i + [num]
                subres.append(tep)
            res.extend(subres)
        return res

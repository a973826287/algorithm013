#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1
        for sh in t:
            t_dict[sh] = t_dict.get(sh, 0) + 1
        
        if s_dict == t_dict:
            return True
        
        return False

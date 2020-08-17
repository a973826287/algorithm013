#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5':'jkl','6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res =['']
        if len(digits)==0:
            return [] 

        for digit in digits:
            tmp = []
            for i in hashmap[digit]:
                for r in res:
                    tmp.append(r+i)
            res = tmp
        return res

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[len(digits)-i-1] < 9:
               digits[len(digits)-i-1] += 1
               return digits
            elif digits[len(digits)-i-1] == 9:
                if len(digits) - i -1 > 0:
                    digits[len(digits)-1-i] = 0
                if len(digits) - i -1 == 0:
                     digits[len(digits)-1-i] = 0
                     digits[1:len(digits)+1] = digits[:]
                     digits[0] = 1
                     return digits

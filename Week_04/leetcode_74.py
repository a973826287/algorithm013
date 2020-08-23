#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        m = len(matrix)
        n = len(matrix[0])
        total = m*n
        left, right = 0, total-1
        while left <= right:
            mid = (left+right)//2
            i = mid//n
            j = mid%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

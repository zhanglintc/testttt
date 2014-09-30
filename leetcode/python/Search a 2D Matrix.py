# Search a 2D Matrix
# for leetcode problems
# 2014.09.30 by zhanglin

# Problem:
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for item in row:
                if item == target:
                    return True
                    
        return False


# Search in Rotated Sorted Array
# for leetcode problems
# 2014.11.02 by zhanglin

# Problem:
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        for i in A:
            if i == target:
                return A.index(i)
        return -1



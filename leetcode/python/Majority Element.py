# Majority Element
# for leetcode problems
# 2014.12.23 by zhanglin

# Problem:
# Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dikt = {}

        for i in num:
            dikt[i] = dikt.get(i, 0) + 1

        for i in dikt:
            if dikt[i] > len(num) / 2:
                return i



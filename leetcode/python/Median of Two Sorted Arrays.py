# Median of Two Sorted Arrays
# for leetcode problems
# 2014.08.16 by zhanglin

# Problem:
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        new_list = []

        while A != [] and B != []:
            if A[0] < B[0]:
                new_list.append(A.pop(0))
            else:
                new_list.append(B.pop(0))

        if A == []:
            new_list += B
        if B == []:
            new_list += A

        if len(new_list) % 2 == 1:
            return new_list[(len(new_list) - 1) // 2]
        else:
            left  = new_list[(len(new_list) - 1) // 2]
            right = new_list[len(new_list) // 2]
            return (float(left) + float(right)) // 2



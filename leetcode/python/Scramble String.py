# Scramble String
# for leetcode problems
# 2014.12.10 by zhanglin

# Problem:
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        # without this judgment, input "a", "a" will be TLE
        # WTF? it works fine on my local machine without this judgment!
        if sorted(s1) != sorted(s2):
            return False

        if s1 == s2:
            return True

        length = len(s1)
        for i in range(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[:i], s2[length - i:]) and self.isScramble(s1[i:], s2[:length - i]):
                return True

        return False



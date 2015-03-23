# Flatten Binary Tree to Linked List
# for leetcode problems
# 2014.08.25 by zhanglin

# Problem:
# Given a binary tree, flatten it to a linked list in-place.

# For example,
# Given

#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten_helper(self, root, pointer):
        if root == None:
            return pointer

        left  = root.left
        right = root.right

        pointer.right = root
        pointer.left = None
        pointer = pointer.right

        pointer = self.flatten_helper(left, pointer)
        pointer = self.flatten_helper(right, pointer)

        return pointer

    def flatten(self, root):
        pointer = TreeNode(0)
        self.flatten_helper(root, pointer)



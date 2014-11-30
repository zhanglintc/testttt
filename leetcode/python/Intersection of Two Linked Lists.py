#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Intersection of Two Linked Lists
# for leetcode problems
# 2014.11.29 by zhanglin

# Problem:
# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.

# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        lenB = 0
        position = None

        p = headA
        while p:
            p = p.next
            lenA += 1

        p = headB
        while p:
            p = p.next
            lenB += 1

        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        while headA and headB:
            if headA != headB:
                position = None

            if headA == headB and position == None:
                position = headA

            headA = headA.next
            headB = headB.next

        return position



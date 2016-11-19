#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 计算二叉树的深度


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree_depth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        return max(1 + self.tree_depth(pRoot.left), 1 + self.tree_depth(pRoot.right))

if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.left.left = TreeNode(2)
    t.left.right = TreeNode(2)
    t.right = TreeNode(2)
    t.right.right = TreeNode(2)
    t.right.right.right = TreeNode(2)

    print(Solution().tree_depth(t))

    p = TreeNode(1)
    print(Solution().tree_depth(p))

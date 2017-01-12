# -*- coding:utf-8 -*-
"""
二叉搜索树
"""


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def inorder_tree_walk(self, node):
        """
        中序遍历二叉树
        :param node: 当前处理节点
        :return: None
        """
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.value, end=", ")
            self.inorder_tree_walk(node.right)

    def tree_insert(self, value):
        """
        二叉树插入操作
        :param value: 待插入节点的值
        :return: node, 也就是插入的节点
        """
        temp = None
        parent = self.root
        node = TreeNode(value)
        while parent is not None:
            temp = parent
            if node.value < parent.value:
                parent = parent.left
            else:
                parent = parent.right
        node.parent = temp
        if temp is None:
            # 空树
            self.root = node
        elif node.value < temp.value:
            temp.left = node
        else:
            temp.right = node
        return node


class TreeNode:
    """二叉树的节点定义"""
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

if __name__ == '__main__':
    root = TreeNode(10)
    tree = BinarySearchTree(root)
    tree.tree_insert(12)
    tree.tree_insert(9)
    tree.inorder_tree_walk(tree.root)

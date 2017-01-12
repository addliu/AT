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

    def tree_search(self, value):
        """
        二叉树查询操作
        :param value: 待查询的值
        :return: 匹配的第一个节点或空
        """
        node = self.root
        while node is not None and node.value != value:
            if node.value < value:
                node = node.right
            else:
                node = node.left
        return node

    def tree_minimum(self, node):
        """返回以node为根的子树中值最小的节点"""
        mini = node
        while mini.left is not None:
            mini = mini.left
        return mini

    def tree_maximum(self, node):
        """返回以node为根的子树中值最大的节点"""
        maxi = node
        while maxi.right is not None:
            maxi = maxi.right
        return maxi

    def tree_insert(self, value):
        """
        二叉树插入操作：未待插入节点找到父节点，为父节点确定待插入节点的左右位置
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

    def tree_successor(self, node):
        """树中给定节点的后继节点"""
        if node.right is not None:
            return self.tree_minimum(node.right)
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = y.parent
        return y

    def tree_predecessor(self, node):
        """树中给定节点的前驱节点"""
        if node.left is not None:
            return self.tree_maximum(node.left)
        y = node.parent
        while y is not None and node == y.left:
            node = y
            y = y.parent
        return y

    def transplant(self, v, u):
        """移动子树"""
        pass

    def tree_delete(self, value):
        """二叉树的删除节点操作"""
        pass


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
    for value in range(0, 101, 2):
        tree.tree_insert(value)
    assert tree.tree_maximum(tree.root).value == 100
    assert tree.tree_minimum(tree.root).value == 0
    assert tree.tree_predecessor(tree.tree_search(50)).value == 48
    assert tree.tree_successor(tree.tree_search(50)).value == 52
    tree.inorder_tree_walk(tree.root)

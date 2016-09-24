#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 基础数据结构： 双向链表 面向对象实现

# 链表类，只存链表的头指针
class LinkedKList(object):
    def __init__(self, value=None):
        self.head = LinkedListNode(value)

    # 在链表中搜索值为value的节点
    def list_search(self, value):
        # 用于储存搜索到的节点
        result = []
        if self.head is None:
            print("链表为空.")
            return result
        else:
            temp = self.head
            while temp is not None:
                if temp.value == value:
                    result.append(temp)
                temp = temp.next
        if len(result) == 0:
            print("链表中不存在值为%s的元素" % value)
            return result

        return result

    # 向链表中插入新节点，采用头插法，即新元素插入表头
    def list_insert(self, value):
        node = LinkedListNode(value)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        node.prev = None

    # 从链表中删除值尾value的元素
    def list_delete(self, value):
        if self.head is None:
            print("链表为空.")
            return
        result = self.list_search(value)
        for node in result:
            # 删除表头元素
            if node.prev is None:
                self.head = node.next
            else:
                node.prev.next = node.next
            # 删除表尾元素
            if node.next is not None:
                node.next.prev = node.prev
            del node


# 链表节点类，定义节点的数据结构
class LinkedListNode(object):
    def __init__(self, obj):
        self.value = obj
        self.prev = None
        self.next = None


if __name__ == '__main__':
    L = LinkedKList(0)
    for i in range(1, 10):
        L.list_insert(i)
    temp = L.head
    while temp.next is not None:
        print(temp.value)
        temp = temp.next

    re = L.list_search(5)
    print(len(re))

    L.list_delete(5)

    re = L.list_search(5)
    print(len(re))
    L.list_delete(5)

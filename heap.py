#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Heap(object):
    def __init__(self, value=list()):
        self.heap_size = len(value)
        self.heap = value
        self.build_max_heap(self.heap)
        
    def parent(self, i):
        """
        求下表为i的节点的父节点
        :param i: 节点i的下标
        :return: None
        """
        if i == 0 or i == 1:
            return 0
        elif i > 1:
            return (i-1) >> 1
        else:
            return -1

    def left(self, i):
        """
        求i节点的左孩子节点下标
        :param i: 节点i的下标
        :return: None
        """
        return (i << 1) + 1

    def right(self, i):
        """
        求i节点的右孩子节点下标
        :param i: 节点i的下标
        :return: None
        """
        return i+1 << 1

    def max_heapify(self, i):
        """
        将i节点的子树大根堆化，维护堆的性质
        :param i : 未排序子树根节点的下标
        :return: 无返回值
        """
        left = self.left(i)
        right = self.right(i)
        if left < self.heap_size and self.heap[left] > self.heap[i]:
            largest = left
        else:
            largest = i
        if right < self.heap_size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def build_max_heap(self, li):
        """
        将给定数组转变成符合堆性质的数组
        :param li: 用于初始化堆的数组
        :return: None
        """
        length = len(li)
        if length != 0:
            for i in range(length//2, -1, -1):
                self.max_heapify(i)

    def heap_sort(self):
        """
        堆排序算法
        算法原理：
        a.构造大(小)根堆，则根节点一定最大(小)，假设为heap[0..n-1]
        b.将根节点heap[0]与heap[n-1]节点互换，则最大(小)值在当前数组最后位置
        c.从堆中去掉最后节点heap[n-1](这一操作通过减少heap.heap_size的值实现)
        此时，剩余节点中，原来根的孩子节点仍然是大(小)根堆，而新的根节点可能违背该性质
        d.对新堆调用heap.max_heapify(0),从新在heap[0..n-2]上构造新的堆
        e.重复调用过程a、b、c、d，直到堆的大小从n-1降到2
        :return: 返回排序后的数组
        """
        length = len(self.heap)
        for i in range(length-1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heap_size -= 1
            self.max_heapify(0)
        self.heap_size = length     # 还原堆的大小
        return self.heap

    def show(self):
        """
        打印堆的信息
        :return: None
        """
        print("堆的长度为:%s" % self.heap_size)
        for i in self.heap:
            print(i, end=' ')
        print()

    def insert(self, values):
        """
        向堆中插入新的值
        :param values:  待插入的值
        :return: None
        """
        self.heap_size += 1
        self.heap.append(values)
        for i in range(self.heap_size//2, -1, -1):
            self.max_heapify(i)

    def search(self, values, index=0):
        """
        在堆中获取元素的位置，返回index
        :param values: 元素的值
        :param index: 下一个与该元素比较的节点的index
        :return: 元素在堆中的位置
        """
        if values > self.heap[index]:
            return -1
        elif values == self.heap[index]:
            return index
        else:
            self.search(values, self.left(index))
            self.search(values, self.right(index))



# 模块测试
if __name__ == '__main__':
    l = [7, 4, 3, 1, 2, 9, 10, 54, 32, 44, 65]
    h = Heap(l)
    h.show()
    h.heap_sort()
    h.show()

#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Heap(object):
    def parent(self, i):
        return i >> 1

    def left(self, i):
        return i << 1

    def right(self, i):
        return i << 1 + 1

    '''
    从a[i], a[left(i)], a[right(i)] 中求最大值,并将下标存储在largest中。
    '''

    def max_heapify(self, a, i):
        l = self.left(i)
        r = self.right(i)
        if l <= a.heap_size and a[l] > a[i]:
            largest = l
        else:
            largest = i
        if r <= a.heap_size and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.max_heapify(a, largest)

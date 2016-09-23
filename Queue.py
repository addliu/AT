#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 基础数据结构：队列 用list()实现


class Queue(object):
    def __init__(self, length):
        object.__init__(self)
        self.queue = [object for index in range(0, length)]
        self.length = length
        self.__head__ = 0
        self.__tail__ = 0

    # 判断栈是否为空
    def is_empty(self):
        if self.__head__ == self.__tail__:
            return True
        return False

    # 判断栈是否满
    def is_full(self):
        if (self.__tail__+1) % self.length == self.__head__:
            return True
        return False

    # 入队操作
    def enter_queue(self, obj):
        if self.is_full():
            print("[Error]:满队列不能执行入队操作")
            return
        self.queue[self.__tail__] = obj
        self.__tail__ = (self.__tail__+1) % self.length

    # 出队操作
    def delete_queue(self):
        if self.is_empty():
            print("[Error]:空队列不能执行出队操作")
            return
        self.__head__ = (self.__head__+1) % self.length

    def __str__(self):
        string = ("队列长度为:%s" % self.length + '\n')
        string += "队列中元素如下:\n"
        if not q.is_empty():
            # 遍历元素，如果tail大于等于head，遍历范围为[head, tail)
            # 如果tail小于head，遍历范围为[head, length)U[0, tail)
            if self.__tail__ >= self.__head__:
                for index in range(self.__head__, self.__tail__):
                    string += str(self.queue[index]) + ', '
            else:
                for index in range(self.__head__, self.length):
                    string += str(self.queue[index]) + ', '
                for index in range(0, self.__tail__):
                    string += str(self.queue[index]) + ', '
            # 去除字符串末尾的 ', ' 两个字符
            string = string[:-2]
        string += '\n'
        string += ("队首在第%s个位置" % (self.__head__ + 1) + '\n')
        string += ("队尾在第%s个位置" % (self.__tail__ + 1) + '\n')
        return string


if __name__ == '__main__':
    print("情输入队列的长度n：")
    n = int(input())
    q = Queue(n)
    for i in range(0, 10):
        q.enter_queue(i)
    print(q)
    for i in range(0, 5):
        q.delete_queue()
    print(q)

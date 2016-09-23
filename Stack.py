#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 基础数据结构：栈 用list()实现


class Stack(object):
    def __init__(self, length):
        object.__init__(self)
        self.stack = [object() for index in range(0, length)]
        self.length = length
        self.__top__ = 0

    # pop函数,出栈操作,删除栈顶元素
    def pop(self):
        if self.is_empty():
            print("[Error]:stack under flow!!!")
            return
        self.__top__ -= 1

    # push函数,入栈操作,将元素压入栈中
    def push(self, obj):
        if self.__top__ >= self.length - 1:
            print("[Error]:stack over flow!!!")
            return
        self.stack[self.__top__] = obj
        self.__top__ += 1

    # 返回栈的信息
    def __str__(self):
        object.__str__(self)
        string = ("栈长度为:%s" % self.length + '\n')
        string += "栈中元素如下:\n"
        for index in range(0, self.__top__):
            string += str(self.stack[index]) + ', '
        # 去除字符串末尾的 ', ' 两个字符
        string = string[:-2]
        string += '\n'
        string += ("栈顶在第%s个位置" % (self.__top__ + 1) + '\n')
        return string

    # 判断栈是否为空
    def is_empty(self):
        if self.__top__ == 0:
            return True
        return False


if __name__ == '__main__':
    print("请输入n：")
    n = int(input())
    s = Stack(n)
    for i in range(0, 10):
        s.push(i)
    print(s)
    for i in range(0, 5):
        s.pop()
    print(s)


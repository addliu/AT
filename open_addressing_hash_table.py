# -*- coding:utf-8 -*-
"""
大小固定的 hash table
开放寻址法(open addressing)
散列函数使用除法散列函数
"""
from clint.textui import colored


class HashTable:
    _DELETED = -100

    def __init__(self, size=0):
        """
        构造函数，初始化 hash table 以及表的大小
        :param size: hash table 的大小
        """
        self.table = [None for index in range(0, size)]
        self.size = size

    def __h(self, key, i):
        """
        使用除法散列函数计算当前 key 在偏移量为 i 时对应的下标
        :param key: 值
        :param i: 偏移量
        :return: key 经过散列后的下标
        """
        index = (key % self.size + i) % self.size
        return index

    def hash_insert(self, key):
        """
        向 hash table 中插入新值 key
        :param key: 待插入的值
        :return: 如果成功插入，则返回插入处的下标，否则返回 None
        """
        i = 0
        while i < self.size:
            j = self.__h(key, i)
            if self.table[j] is None or self.table[j] == self._DELETED:
                self.table[j] = key
                # self.size += 1
                print(colored.green('插入成功，值 {} 已成功插入'.format(key)))
                return j
            else:
                i += 1
        print(colored.red('插入失败， hash table 已满！'))
        return None

    def hash_search(self, key):
        """
        在 hash table 中查找值 key 对应的下标
        :param key: 待查找的值
        :return: key 的下标或 None
        """
        i = 0
        j = self.__h(key, i)
        while i < self.size or self.table[j] is None:
            j = self.__h(key, i)
            if self.table[j] == key:
                print(colored.green('成功在下标 {} 处找到值 {}  '.format(j, key)))
                return j
            i += 1
        print(colored.red('当前 hash table 中未找到值 {} ！'.format(key)))
        return None

    def hash_delete(self, key):
        """
        从 hash table 中删除值为 key 的元素
        :param key: 待删除的元素
        :return: key 的下标或 None
        """
        index = self.hash_search(key)
        if index is None:
            print(colored.red('删除失败， {} 不在当前 hash table 中！'.format(key)))
            return None
        else:
            self.table[index] = self._DELETED
            # self.size -= 1
            print(colored.green('删除成功，{} 的下标为 {}'.format(key, index)))
            return index

# 测试脚本
if __name__ == '__main__':
    l = [i for i in range(0, 7)]
    table = HashTable(7)
    for i in l:
        table.hash_insert(i)

    table.hash_delete(5)
    table.hash_delete(5)
    table.hash_search(5)
    table.hash_insert(100)
    table.hash_insert(10)
    table.hash_search(100)
    table.hash_search(50)

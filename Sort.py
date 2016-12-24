# -*- coding:utf-8 -*-
class Sort(object):

	def quicksort(self, arr):
		"""
		使用快速排序对 arr 进行排序
		:param arr: 待排序序列
		:return : 排序后的 list
		"""
		if len(arr) <= 1:
			return arr
		pivot = arr[len(arr)//2]
		left = [x for x in arr if x < pivot]
		middle = [x for x in arr if x == pivot]
		right = [x for x in arr if x > pivot]
		return self.quicksort(left) + middle + self.quicksort(right)


if __name__ == '__main__':
	print(Sort().quicksort([3, 6, 8, 10, 1, 2, 1]))

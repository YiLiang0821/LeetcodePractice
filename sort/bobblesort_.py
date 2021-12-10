#-*- coding: utf-8 -*-
"""

@author: YiLiang
"""
print('bobblesort algo pratice')
"""
if we have n elements, it will do n-1 times
"""
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import random

#隨機產生變數進行排序
data = random.sample(range(100),10)
count = len(data)

def showdata(data):
	print('原始資料:')
	for i in range(len(data)):
		print('%d' %data[i],end = ' ')
	print('\n--------------------------')

def bobblesort(data):
	for i in range(count-1,-1,-1):
		for j in range(i):
			if data[j] > data[j+1]:
				data[j],data[j+1] = data[j+1],data[j]
		print('第%d次排序:' %(count-i))

		for j in range(count):
			print('%3d' %data[j],end = ' ')
		print()


	print('sort result:')
	for k in range(count):
		print(data[k],end = ' ')
showdata(data)
bobblesort(data)


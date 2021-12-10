#-*- coding: utf-8 -*-
"""
Selection Sort Pratice

@author: YiLiang
"""
#enable encoding
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import random
data = random.sample(range(100),10)

def showdata(data):
	print('原始資料:')
	for i in range(len(data)):
		print('%d' %data[i],end = ' ')
	print('\n--------------------------')

def sortprocess(data):
	for i in range(len(data)-1):
		for j in range(i+1,len(data)):  #自己不跟自己比
			if data[i] > data[j]:
				data[i],data[j] = data[j],data[i]

		print('第%d次' %(i+1),data)
		
		print()
	print('排序後：',data)
showdata(data)
sortprocess(data)


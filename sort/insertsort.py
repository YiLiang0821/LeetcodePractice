#-*- coding: utf-8 -*-
"""
Insert Sort Pratice

@author: YiLiang
"""
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import random
import time
data = random.sample(range(100),5)

def showdata(data):
	print('原始資料:')
	for i in range(len(data)):
		print('%d' %data[i],end = ' ')
	print('\n--------------------------')
def insertprocess(data):
	
	for i in range(1,len(data)): #從第二個開始比較
		temp = data[i]           #temp為一個暫存
		j = i -1
		while j >= 0 and temp<data[j]:
			data[j+1] = data[j]
			j = j-1 #一個一比較

		data[j+1] = temp

		print('第%d次排序'%i,data)
def main():
	showdata(data)
	insertprocess(data)

T_start = time.time()
main()
T_end = time.time()
print(T_start - T_end)

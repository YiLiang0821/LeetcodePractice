#-*- coding: utf-8 -*-
"""
Shell Sort Pratice

@author: YiLiang
"""
import random
import time

def showdata(data):
	for i in range(len(data)):
		print('%d' %data[i],end = ' ')
	print('\n--------------------------')

def shell(data,size):
	k = 1							#計數器
	jmp = size//2					#幾個幾個為一區隔，最好是質數
	while jmp != 0 :
		for i in range(jmp, size):	#jmp為設定區間
			tmp = data[i]
			j = i - jmp 			#從前面數的第幾個
			while tmp < data[j] and j >= 0:	#compare value, like insert sort
				data[j + jmp] = data[j]
				j = j-jmp
			data[jmp + j] = tmp
		print('第%d次排序:'%k, end = '')
		k = k+1
		showdata(data)
		jmp = jmp // 2
def main():
	data = random.sample(range(100),8)
	SIZE = len(data)
	print('原始陣列：')
	showdata(data)
	print('開始shell sort : ')
	shell(data,SIZE)

T_start = time.time()
main()
T_end = time.time()
print(T_start - T_end)

'''
第 008 题：
输出 9*9 乘法口诀表
'''

for i in range(1, 10):
	print()
	for j in range(1, i+1):
		print('{}*{}={} '.format(i, j, i*j), end='')
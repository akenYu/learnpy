'''
第 009 题：
暂停五秒循环输出，并格式化当前时间
'''

import time

for i in range(10):
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
	time.sleep(5)
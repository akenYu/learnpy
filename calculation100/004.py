'''
第 004 题：
输入某年某月某日，判断这一天是这一年的第几天？
'''

import time


date = input('请输入日期，格式如xxxx-xx-xx: ')
days = time.strptime(date, '%Y-%m-%d').tm_yday
print('这一天是这一年的第 %s 天' % days)
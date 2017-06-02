'''
第 005 题：
输入三个整数x,y,z，请把这三个数由小到大输出
'''

num = input('输入三个数字：')
li = [int(i) for i in num.split()]
li.sort()
print(li)
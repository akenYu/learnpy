'''
第 001 题：
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

num = [1, 2, 3, 4]


result = [i*100 + j*10 + k for i in num for j in num
		  for k in num if (i != j and i != k and j != k)]
print(result, '\n', len(result))
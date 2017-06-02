'''
第 006 题：
斐波那契数列。指的是这样一个数列：0、1、1、2、3、5、8、13、21..
'''

# 方法一
def fib1(n):
	a, b = 1, 1
	for i in range(n-1):
		a, b = b, a + b
	return a


# 方法二：使用递归
def fib2(n):
	if n == 1 or n == 2:
		return 1
	return fib2(n-1)+fib2(n-2)


# 方法三：输出数列
def fib3(n):
	if n == 1:
		return [1]
	if n == 2:
		return [1, 1]
	fibs = [1, 1]
	for i in range(2, n):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs


# 方法四：使用生成器
def fib4(n):
	c, a, b = 0, 0, 1
	while c < n:
		yield b
		a, b = b, a + b
		c += 1


if __name__ == '__main__':
	print(fib1(10))
	print(fib2(10))
	print(fib3(10))
	for i in fib4(10):
		print(i)
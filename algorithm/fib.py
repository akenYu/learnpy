# 定义斐波拉契生成器函数

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1


if __name__ == '__main__':
	for i in fib(30):
		print(i)
# 定义一个函数quadratic(a, b, c), 返回ax^2 + bx + c = 0的两个解

import math


def quadratic(a, b, c):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(b, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(c, (int, float)):
		raise isinstance('bad operand type')

	if a == 0:
		return '有唯一解：%f' % (- (c / b)) 
	else:
		temp = b ** 2 - 4 * a * c
		if temp < 0:
			return '无解'
		elif temp == 0:
			return '有唯一解：%f' % (-b / (2 * c))
		else:
			x1 = (-b + math.sqrt(temp)) / (2 * a)
			x2 = (-b - math.sqrt(temp)) / (2 * a)
			return x1, x2


if __name__ == '__main__':
	print(quadratic(2, 3, 1))
	print(quadratic(1, 3, -4))
	print(quadratic(0, 3, 1))
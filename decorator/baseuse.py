# 装饰器的基本用法

import functools


# 定义不带参数的装饰器
def nonparm(func):
	@functools.wraps(func) # 将原始函数的属性复制到返回函数中
	def wrapper(*args, **kwargs):
		print('call %s()' % func.__name__)
		return func(*args, **kwargs)
	return wrapper


@nonparm
def now():
	print('1-2017-05-24')


# 定义带参数的装饰器
def haveparm(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kwargs) 
		return wrapper
	return decorator


@haveparm('hello')
def now2():
	print('2-2017-05-24')


# 编写一个装饰器，能在函数调用的前后打印出'begin call'和'end call'的日子
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print('bigin call %s()' % func.__name__)
		func(*args, **kwargs)
		print('end call %s()' % func.__name__)
	return wrapper


@log
def now3():
	print('3-2017-05-24')


# 编写一个即支持不带参数，又支持可带参数的装饰器
def log2(parmfunc):
	if isinstance(parmfunc, str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kwargs):
				print('%s %s()' % (parmfunc, func.__name__))
				func(*args, **kwargs)
			return wrapper
		return decorator
	else:
		@functools.wraps(parmfunc)
		def wrapper(*args, **kwargs):
			print('call %s()' % parmfunc.__name__)
			parmfunc(*args, **kwargs)
		return wrapper


@log2
@log2('hi')
def now4():
	print('4-2017-05-24')


if __name__ == '__main__':
	now()
	now2()
	now3()
	now4()
# 多个线程同时操作一个变量，内容会被改乱
# 使用lock确保某段关键代码只能由一个线程从头到尾完整的执行

import time, threading

balance = 0
lock = threading.Lock()


def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n


def run_thread(n):
	for i in range(1000000):
		lock.acquire() # 要先获取锁
		try:
			change_it(n)
		finally:
			lock.release() # 最后要释放锁


if __name__ == '__main__':
	t1 = threading.Thread(target=run_thread, args=(5,))
	t2 = threading.Thread(target=run_thread, args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)
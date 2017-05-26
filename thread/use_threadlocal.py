# 使用ThreadLocal解决参数在一个线程中各个函数之间互相传递的问题

import threading

local_school = threading.local()


def process_student():
	std = local_school.student
	print('hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
	local_school.student = name
	process_student()


if __name__ == '__main__':
	t1 = threading.Thread(target=process_thread, args=('A'), name='Tread-A')
	t2 = threading.Thread(target=process_thread, args=('B'), name='Tread-B')
	t1.start()
	t2.start()
	t1.join()
	t2.join()
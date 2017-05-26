import os, time, random
from multiprocessing import Process, Queue


def write(q):
	print('process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('put %s to queue' % value)
		q.put(value)
		time.sleep(random.random())


def read(q):
	print('process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('get %s from queue' % value)


if __name__ == '__main__':
	# 父进程创建queue，并传给各个子进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	# pr进程里是死循环，无法等待结束，只能强行终止
	pr.terminate()
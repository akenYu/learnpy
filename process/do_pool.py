# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程

import os, time, random
from multiprocessing import Pool


def long_time_task(name):
	print('run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
	print('parent process %s.' % os.getpid())
	p = Pool(5)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('waiting for all subprocesses done...')
	p.close()
	p.join() # 等待所有子进程执行完毕
	print('all subprocesses done')
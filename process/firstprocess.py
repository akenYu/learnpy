from multiprocessing import Process
import os


def run_proc(name):
	print('run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
	print('parent process %s' % os.getpid())
	p = Process(target=run_proc, args=('text',))
	print('child process will start')
	p.start()
	print('1')
	p.join()
	print('2')
	print('child process end')
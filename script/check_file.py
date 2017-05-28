# 检测文件是否存在并读取内容

import sys, os


def readfile(filename):
	print(filename)
	f = open(filename, 'r')
	line = f.read()
	print(line)


def main():
	# filename = ''
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print('[-] ' + filename + ' does not exist')
			exit(0)
		if not os.access(filename, os.R_OK):
			print('[-] ' + filename + ' access denied')
			exit(0)
		print('[+] Reading from : ' + filename)
		readfile(filename)
	return


if __name__ == '__main__':
	main()
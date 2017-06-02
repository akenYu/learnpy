# 简单的dns正向查询功能

import sys, socket


def print_array(*args):
	array = args
	for item in array:
		print(item[4][0])


def start_check():
	print('''this script is for host resolve
now this begin
if you want to leave, please input 'break' ''')
	while True:
		try:
			host = input('please input the host(like www.baidu.com):\n')
		except KeyboardInterrupt:
			print('\n')
			continue
		if host == 'break' or host == '':
			break
		# getaddrinfo(host, port[,family[, sockettype[, proto[, flags]]]])
		result = socket.getaddrinfo(host, None, 0, socket.SOCK_STREAM)
		print_array(*result)

if __name__ == '__main__':
	start_check()
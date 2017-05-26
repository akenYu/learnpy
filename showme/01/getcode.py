# 第 0001 题：生成200个激活码，并保存在文件中

import random, string


def get_string(num, length=10):
	f = open('code.txt', 'w')
	chars = string.ascii_uppercase + string.digits
	for i in range(num):
		one_code = random.sample(chars, length)
		f.write(''.join(one_code) + '\n')
	f.close()


if __name__ == '__main__':
	get_string(200)
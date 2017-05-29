# 第 0007 题：统计目录里面的程序，写过多少行代码，包括空行和注释，分别列出来

import os


def countcode(dirname):
	blanknum = 0
	comments = 0
	totalnum = 0
	mc_flag = False

	for root, dirs, files in os.walk(dirname):
		for path in files:
			if not path.endswith('.py'):
				continue
		
			filepath = os.path.join(root, path)
			for count, line in enumerate(open(filepath, 'rU', encoding='utf-8')):
				totalnum += 1
				# 判断空行数
				temp = line.strip()
				if temp == '':
					blanknum += 1

				# 判断单行注释数
				elif temp[0] == '#':
					comments += 1

				# 判断多行注释数
				else:
					if False == mc_flag:
						if temp[0:3] == '"""''"""':
							mc_flag = True
						elif temp[-3:] == '"""':
							mc_flag = False
							comments += 1
					if mc_flag:
						comments += 1

	print('总空格：%s\n总注释：%s\n总代码：%s' % (blanknum, comments, totalnum))
	return None


if __name__ == '__main__':
	countcode('.')
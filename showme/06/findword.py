# 第 0006 题：在一个只有txt格式且内容都是英文的文件目录中
# 统计你认为每篇日记最重要的词（即出现最多的那个词）

import os


def findword(dirpath):
	if dirpath is None:
		return None

	for files in os.listdir(dirpath):
		if not files.endswith('.txt'):
			continue
		filepath = os.path.join(dirpath, files)
		content = open(filepath, 'r').read().lower()
		words = content.split()
		worddic = {}
		for word in words:
			if word in worddic.keys():
				worddic[word] += 1
			else:
				worddic[word] = 1
		if len(worddic):
			mostword = max(worddic.items(), key=lambda x: x[1])
			mostkey, mostvalue = mostword
			print('%s : %s -- %s' % (files, mostkey, mostvalue))


if __name__ == '__main__':
	findword('.')
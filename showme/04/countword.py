# 第 0004 题：任一个英文纯文本文件，统计其中的单词出现的个数

filename = 'hello.txt'

line_counts = 0
word_counts = 0
char_counts = 0


with open(filename, 'r') as f:
	for line in f:
		word = line.split()
		line_counts += 1
		word_counts += len(word)
		char_counts += len(line)


if __name__ == '__main__':
	print('line counts', line_counts)
	print('word counts', word_counts)
	print('char_counts', char_counts)
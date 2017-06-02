# 第 0012 题：敏感词文本文件 filtered_words.txt，当用户输入敏感词语，
# 则用 星号 * 替换


def replaceword(path):
	word_list = []
	with open(path, 'r') as f:
		for word in f.read().split():
			word_list.append(word)
	# print(word_list)
	
	inp = input('请输入一个句子：')
	for i in word_list:
		if i in inp:
			print(inp.replace(i, '*'))


if __name__ == '__main__':
	replaceword('filted_words.txt')
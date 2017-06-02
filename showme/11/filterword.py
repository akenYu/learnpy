# 第 0011 题：敏感词文本文件 filtered_words.txt，当用户输入里
# 面的敏感词语时，则打印出 Freedom，否则打印出 Human Rights


def filterword(path):
	word_list = []
	with open(path, 'r') as f:
		for word in f.read().split():
			word_list.append(word)
	print(word_list)
	
	while True:
		inp = input('请输入一个词语：')
		if inp == 'break':
			break
		elif inp in word_list:
			print('Freedom')
		else:
			print('Human Rights')


if __name__ == '__main__':
	filterword('filted_words.txt')
# 第 0008 题：一个HTML文件，找出里面的正文
# 不要用windows的cmd运行！！！

import re
import requests
from bs4 import BeautifulSoup


def get_body(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.content.decode('utf-8'), 'html.parser')
	
	# 清理html结尾的script和style
	[script.extract() for script in soup.find_all('script')]
	[style.extract() for style in soup.find_all('style')]
	soup.prettify()

	# 清理所有html的标签
	reg = re.compile('<[^>]*>')
	ret_content = reg.sub('', soup.prettify())
	print(ret_content)


if __name__ == '__main__':
	get_body('http://www.baidu.com')
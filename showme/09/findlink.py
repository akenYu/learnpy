# 第 0009 题：一个HTML文件，找出里面的链接
# 不要用windows的cmd运行！！！

import re
import requests
from bs4 import BeautifulSoup


def get_link(url):
	page = requests.get(url).text
	soup = BeautifulSoup(page, 'html.parser')
	links = soup.find_all(name='a', attrs={'href':re.compile(r'^https?:')})
	for link in links:
		print(link.get('href'))


if __name__ == '__main__':
	get_link('https://www.baidu.com/')
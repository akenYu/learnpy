# 一道面试题：编写一个脚本,使用方式：
# main.py -u http://www.sohu.com -d 'a=1,b=2,c=3' -o /index.html
# 功能要求：打开-u指定的页面，将页面中所有的链接后面增加参数a=1&b=2&c=3
# 需要考虑链接中已经存在指定参数的问题，然后保存到-o指定的文件

import argparse
import urllib
from pyquery import PyQuery as pq


def getargs():
	parse = argparse.ArgumentParser()
	parse.add_argument('-u', type=str)
	parse.add_argument('-d', type=str)
	parse.add_argument('-o', type=str)
	args = parse.parse_args()
	return vars(args)


def urladdquery(url, query):
	query = query.replace(',', '&')
	if '?' in url:
		return url.replace('?', '?'+query+'&')
	else:
		return url + '?' + query


def gethref():
	args = getargs()
	url = args['u']
	query = args['d'].strip("\'")
	filename = args['o']
	doc = pq(url=url)
	with open(filename, 'w') as f:
		for a in doc('a'):
			a = pq(a)
			href = a.attr('href')
			if href:
				newurl = urladdquery(href, query)
				f.write(newurl + '\n')


if __name__ == '__main__':
	gethref()
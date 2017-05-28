# 查询ip、网址归属地

import re, sys
import urllib.request


def isip(s):
	return len([i for i in s.split('.') if (0 <= int(i) <=255)]) == 4


def url(ip):
	uip = urllib.request.urlopen('http://wap.ip138.com/ip.asp?ip=' + ip)
	fip = uip.read().decode('utf-8')
	rip = re.compile('<br/><b>查询结果：(.*)</b><br/>')
	result = rip.findall(fip)
	print('%s %s' % (ip, result[0]))


def do(domain):
	url = urllib.request.urlopen('http://wap.ip138.com/ip.asp?ip=' + domain)
	fdomain = url.read().decode('utf-8')
	rdomain = re.compile('<br/><b>查询结果：(.*)</b><br/>')
	result = rdomain.findall(fdomain)
	print('%s %s' % (domain, result[0]))


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('请输入ip地址或域名（例如：192.168.1.1 / www.baidu.com）')
		sys.exit()
	youinput = sys.argv[1]
	if not re.findall('(\d{1,3}\.){3}\d{1,3}', youinput):
		if re.findall('(\w+\.)?(\w+)(\.\D+){1,2}', youinput):
			do(youinput)
		else:
			print('输入的ip或域名格式不对')
	else:
		if isip(youinput):
			url(youinput)
		else:
			print('ip地址不合法，请重新输入')
# 第 0002 题：生成的200个激活码保存在mysql关系型数据库中

import random, string
import pymysql


def get_string(num, length=10):
	codes = []
	chars = string.ascii_uppercase + string.digits
	for i in range(num):
		one_code = random.sample(chars, length)
		codes.append(''.join(one_code))
	return codes


def save_code_mysql():
	try:
		conn = pymysql.connect(host='localhost', user='root', password='123456', charset='UTF8')
		cur = conn.cursor()
	except BaseException as e:
		print(e)
	else:
		try:
			cur.execute("CREATE DATABASE IF NOT EXISTS code_mysql")
			cur.execute("USE code_mysql")
			cur.execute("CREATE TABLE IF NOT EXISTS codes (id INT AUTO_INCREMENT PRIMARY KEY, code VARCHAR(32))")

			codes = get_string(200)
			for code in codes:
				cur.execute("INSERT INTO codes(code) values(%s)", (code))
			conn.commit()

			cur.execute("SELECT * FROM codes")
			result = cur.fetchall()
			for i in result:
				print(i)
		except BaseException as e:
			print(e)
	finally:
		cur.close()
		conn.close()


if __name__ == '__main__':
	save_code_mysql()
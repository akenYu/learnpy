# 第 0003 题：生成的200个激活码保存在Redis非关系型数据库中

import random, string
import redis


def get_string(num, length=10):
	codes = []
	chars = string.ascii_uppercase + string.digits
	for i in range(num):
		one_code = random.sample(chars, length)
		codes.append(''.join(one_code))
	return codes


def save_code_redis():
	r = redis.Redis(host='localhost', port=6379, db=0)
	codes = get_string(200)
	# 管道可以充当“批处理”的工具，在一定程度上提升性能
	# p = r.pipeline() 
	for code in codes:
		r.sadd('codes', code)
	# p.execute()
	print(r.scard('codes'))
		

if __name__ == '__main__':
	save_code_redis()
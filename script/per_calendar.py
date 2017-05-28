# 用Python实现万年历

def leap_year(year):
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		return True
	else:
		return False


def get_month_days(year, month):
	days = 31
	if month == 2:
		if leap_year(year):
			days = 29
		else:
			days = 28
	elif month == 4 or month == 6 or month == 9 or month == 11:
		days = 30
	return days


def get_total_days(year, month):
	totaldays = 0
	for i in range(1, year):
		if leap_year(i):
			totaldays += 366
		else:
			totaldays += 365
	for i in range(1, month):
		totaldays += get_month_days(year, i)
	return totaldays

def main():
	year = int(input('请输入年份：'))
	month = int(input('请输入月份：'))
	icount = 0
	i = 1
	print('日\t一\t二\t三\t四\t五\t六')
	for i in range(get_total_days(year, month) % 7 + 1):
		print('\t', end='')
		icount += 1
	for i in range(1, get_month_days(year, month) + 1):
		print(i, '\t', end='')
		icount += 1
		if icount % 7 == 0:
			print('')


if __name__ == '__main__':
	main()
"""
learn_oneline.py
~~~~~~~~~~~~~~~~

只用一行代码实现的程序
"""


# python之禅
# python -c "import this"


# 一行代码启动一个web服务
# python -m http.server 8080


# 一行代码实现变量值互换
a, b = 1, 2; a, b = b, a


# 一行代码解决FizzBuzz问题：打印数字1到100, 3的倍数打印“Fizz”来替换这个数, 5的倍数打印“Buzz”, 既是3又是5的倍数的打印“FizzBuzz”
print('\n'.join('fizz'[x % 3 * 4:] + 'buzz'[x % 5 * 4:] or str(x) for x in range(1, 101)))


# 一行代码输出特定字符"Love"拼成的心形
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


# 一行代码输出Mandelbrot图像: Mandelbrot图像中的每个位置都对应于公式N=x+y*i中的一个复数
print('\n'.join([''.join(['*'if abs((lambda a: lambda z, c, n: a(a, z, c, n))(lambda s, z, c, n: z if n == 0 else s(s, z*z+c, c, n-1))(0, 0.02*x+0.05j*y, 40)) < 2 else ' ' for x in range(-80, 20)]) for y in range(-20, 20)]))


# 一行代码打印九九乘法表
print('\n'.join([''.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))
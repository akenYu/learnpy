# 第 0000 题：将你的头像右上角加上红色的数字

from PIL import Image, ImageDraw, ImageFont


def addnum(img):
	im = Image.open(img)

	out = im.resize((160, 160), Image.ANTIALIAS)
	draw = ImageDraw.Draw(out)
	font = ImageFont.truetype('Arial.ttf', 36)
	draw.text((out.size[0]*0.85, out.size[1]*0.05), '5', font=font, fill='red')
	out.show()
	out.save('test2.jpg', 'jpeg')


if __name__ == '__main__':
	addnum('test.jpg')
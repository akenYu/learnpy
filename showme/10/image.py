# 第 0010 题：使用python生成字母验证码图片

from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random


def rndChar():
	return chr(random.randint(65, 90))


def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def genecode():
	width = 60 * 4
	height = 60
	image = Image.new('RGB', (width, height), (255, 255, 255))
	font = ImageFont.truetype('Arial.ttf', 36)
	draw = ImageDraw.Draw(image)

	for x in range(width):
		for y in range(height):
			draw.point((x, y), fill=rndColor())
	for t in range(4):
		draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

	image = image.filter(ImageFilter.BLUR)
	image.save('code.jpg', 'jpeg')


if __name__ == '__main__':
	genecode()
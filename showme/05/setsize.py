# 第 0005 题：把目录中的所有照片的尺寸变成都不大于iPhone5分辨率的大小

import os
from PIL import Image


def set_imsize(path):
	if path is None:
		return
	for (rootdir, subdir, subfile) in os.walk(path):
		print('rootdir:%s, subdir:%s, subfile:%s' % (rootdir, subdir, subfile))
		for picname in subfile:
			if not picname.endswith('.jpg'):
				continue
			picpath = os.path.join(rootdir, picname)
			with Image.open(picpath) as image:
				if image is not None:
					new_image = image.resize((640, 1136), Image.ANTIALIAS)
					new_image.save('new_'+picname.split('.')[0]+'.jpg', 'jpeg')


if __name__ == '__main__':
	set_imsize('.')
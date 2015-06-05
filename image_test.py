# -*- coding:utf-8 -*-

from PIL import Image
img = Image.open(r'F:\Buccaneer\.git\download_img\diameizi\20150603084446.jpg')
print type(img)
pil_img = img.convert('L')
pil_img.show()
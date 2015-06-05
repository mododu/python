# -*- coding:utf-8 -*-
import math
from PIL import Image

TEST_ADDR1 = r'F:\Buccaneer\.git\download_img\meizitu\20150602115055.jpg'
TEST_ADDR2 = r'F:\Buccaneer\.git\download_img\meizitu\20150602115100.jpg'
TEST_ADDR3 = r'F:\Buccaneer\.git\download_img\meizitu\20150602115220.jpg'

class PixImage(object):

	def __init__(self, addr):
		print 'State:-- Getting image --'
		self.img = Image.open(addr)
		print 'State:-- Get image successfully --'
		self.width = self.img.size[0]
		self.height = self.img.size[1]
		self.local_addr = addr
		self.pix_distribution = {
		'000': 0, '001': 0, '002': 0, '003':0,
		'010': 0, '011': 0, '012': 0, '013':0,
		'020': 0, '021': 0, '022': 0, '023':0,
		'030': 0, '031': 0, '032': 0, '033':0,
		'100': 0, '101': 0, '102': 0, '103':0,
		'110': 0, '111': 0, '112': 0, '113':0,
		'120': 0, '121': 0, '122': 0, '123':0,
		'130': 0, '131': 0, '132': 0, '133':0,
		'200': 0, '201': 0, '202': 0, '203':0,
		'210': 0, '211': 0, '212': 0, '213':0,
		'220': 0, '221': 0, '222': 0, '223':0,
		'230': 0, '231': 0, '232': 0, '233':0,
		'300': 0, '301': 0, '302': 0, '303':0,
		'310': 0, '311': 0, '312': 0, '313':0,
		'320': 0, '321': 0, '322': 0, '323':0,
		'330': 0, '331': 0, '332': 0, '333':0
		}
		self.pix_vector = []

		print 'State:-- Reading image pixel --'
		for h in range(self.height):
			for w in range(self.width):
				pixel = self.img.getpixel((w,h))
				self.analysis_pixel(pixel)
		print 'State:-- Analyse pixel successfully --'
		self.get_pixel_vector()
		print 'State:-- Get pixel vector successfully --'	
	
	def analysis_pixel(self, pixel):
		r_color = pixel[0]
		g_color = pixel[1]
		b_color = pixel[2]
		r_info = ''
		g_info = ''
		b_info = ''
		
		if r_color in range(0  ,64 ):	r_info = '0'
		if r_color in range(64 ,128):	r_info = '1'
		if r_color in range(128,192):	r_info = '2'
		if r_color in range(192,256):	r_info = '3'
		if g_color in range(0  ,64 ):	g_info = '0'
		if g_color in range(64 ,128):	g_info = '1'
		if g_color in range(128,192):	g_info = '2'
		if g_color in range(192,256):	g_info = '3'
		if b_color in range(0  ,64 ):	b_info = '0'
		if b_color in range(64 ,128):	b_info = '1'
		if b_color in range(128,192):	b_info = '2'
		if b_color in range(192,256):	b_info = '3'

		pixel_info = r_info + g_info + b_info
		self.pix_distribution[pixel_info] += 1

	def get_pixel_vector(self):
		for i in '0123':
			for j in '0123':
				for k in '0123':
					key = i + j + k
					self.pix_vector.append(self.pix_distribution[key])
	
	def print_info(self):
		#self.img.show()
		print 'Image Address:',	self.local_addr
		print 'Image Width:  ', self.width
		print 'Image Height: ', self.height

	def show_pix_distribution(self):
		pass

	def contrast(self, other):
		vec1 = self.pix_vector
		vec2 = other.pix_vector
		vec1_module = 0
		vec2_module = 0
		vec_product = 0
		for i in range(64):
			vec1_module += vec1[i] **2
			vec2_module += vec2[i] **2
			vec_product += vec1[i] * vec2[i]
		vec1_module **= 0.5
		vec2_module **= 0.5
		cos_value = vec_product / (vec1_module*vec2_module)
		return math.acos(cos_value)

image1 = PixImage( TEST_ADDR1 )
image2 = PixImage( TEST_ADDR2 )
image3 = PixImage( TEST_ADDR3 )
c12 = image1.contrast(image2)
c23 = image2.contrast(image3)
c13 = image1.contrast(image3)
print c12,'\n',c23,'\n',c13


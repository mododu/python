# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os
import time
import datetime

dir_name = 'baby_metal'
url = 'http://nvse.org/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

now_time = datetime.datetime.now()
time_sign = str(int(time.mktime(now_time.timetuple())))

def write_file(file_name, content):
    tmp = open(file_name, 'w+')
    tmp.write(content)
    tmp.close()

def get_page(url, headers={ 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }):
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    return content

def get_tieba_img(page):
    pic_sign = r'src="(.+?\.jpg)" pic_ext'
    pic_re = re.compile(pic_sign)
    pic_list = re.findall(pic_re, page)
    return pic_list

def download_img(img_list, dir_name):
    if dir_name != '':
        dir_name = dir_name + '\\'
    num = 0
    for imgurl in img_list:
        urllib.urlretrieve(imgurl, os.path.join('F:\Buccaneer\.git\download_img\\'+dir_name+time_sign+str(num)+'.jpg'))
        num += 1
    return num

page = get_page(url, headers)
print page



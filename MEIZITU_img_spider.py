# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os
import time
import datetime
import sys

CALL_TIME = 5
dir_name = 'meizitu'
url = 'http://www.meizitu.com/a/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

#now_time = datetime.datetime.now()
#time_sign = str(int(time.mktime(now_time.timetuple())))

def write_file(file_name, content):
    tmp = open(file_name, 'w+')
    tmp.write(content)
    tmp.close()

def get_page(url, headers={ 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }):
    content = ''
    for i in range(CALL_TIME):
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
        except:
            print '--GET PAGE ERROR!--'
            continue
        if content != '':
            break
    return content

def get_img_list(page):
    pic_sign = r'src="(http://pic.meizitu.com/wp-content/uploads/201\da/\d\d/\d\d/\d\d.*?\.jpg)"'
    pic_re = re.compile(pic_sign)
    pic_list = re.findall(pic_re, page)
    return pic_list

def download_img(img_list, dir_name):
    if dir_name != '':
        dir_name = dir_name + '\\'
    num = 0
    for imgurl in img_list:
        try:
            urllib.urlretrieve(imgurl, os.path.join('F:\Buccaneer\.git\download_img\\'+dir_name+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'))
        except:
            print '--DOWNLOAD IMG ERROR!--'
            continue
        print '--Download image ' + str(imgurl) + '!--'
        time.sleep(1)
        num += 1
    return num


for page_id in range(1, 5000):
    page_url = url + str(page_id) + '.html'
    page = get_page(page_url, headers)
    print '--Get page'+str(page_id)+' successfully!--'
    img_list = get_img_list(page)
    download_img(img_list, dir_name)




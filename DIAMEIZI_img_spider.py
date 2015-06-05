# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os
import time
import datetime
import sys

CALL_TIME = 5
DIR_NAME = 'diameizi'
INDEX_PAGE_URL = 'F:\Buccaneer\.git\python_test\diameizi.htm'
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
HEADERS = { 'User-Agent' : USER_AGENT }

def write_file(file_name, content):
    tmp = open(file_name, 'w+')
    tmp.write(content)
    tmp.close()

def read_file(file_name):
    tmp = open(file_name, 'r')
    content = tmp.read()
    tmp.close()
    return content

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

def get_alinks_list(page):
    alinks_sign = r'<a href="(.+?)" title="全文链接">全文链接</a>'
    alinks_sign_re = re.compile( alinks_sign )
    alinks_pages_list = re.findall( alinks_sign_re, page )
    return alinks_pages_list

def get_imgs_list(page):
    pic_sign = r'<img src="(http://m\d.img.srcdd.com.+?.jpeg)"'
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


'''for page_id in range(3500, 3900):
    page_url = url + str(page_id) + '.html'
    page = get_page(page_url, headers)
    print '--Get page'+str(page_id)+' successfully!--'
    img_list = get_img_list(page)

    download_img(img_list, dir_name)'''


index_page = read_file( INDEX_PAGE_URL )
alinks_list = get_alinks_list( index_page )

for alink_url in alinks_list:
    alink_page = get_page (alink_url, HEADERS)
    print '--Get alink page successfully!--'
    img_list = get_imgs_list(alink_page)
    download_img(img_list, DIR_NAME)


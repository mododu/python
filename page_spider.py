# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os
import time
import datetime
import sys

CALL_TIME = 5
DIR_NAME = r'F:\Buccaneer\.git\save_page'
INDEX_PAGE_URL = 'http://news.163.com/'
USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
HEADERS = { 'User-Agent' : USER_AGENT }

URLS_NUM = 10000
urls_dictionary = { INDEX_PAGE_URL: True }
urls_list = [INDEX_PAGE_URL]

def write_file(file_name, content):
    for i in range(2):
        try:
            tmp = open(file_name, 'w+')
            tmp.write(content)
            tmp.close()
        except:
            print '--WRITE FILE ERROR!--'
            continue
        break

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
    alinks_sign = r'<a.+?href="(.+?)"'
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

def analyse_page(url):
        page = get_page(url, HEADERS)
        file_name = url.replace("?","").replace(".htm","").replace(".html","").replace("http:","http.").replace("/","").replace('\\','').replace("?","_") + '.html'
        file_dir = DIR_NAME +'\\'+ file_name
        print file_name
        write_file(file_dir, page)
        alinks_list = get_alinks_list(page)
        
        for alink_url in alinks_list:    
            if len(urls_list) < URLS_NUM and not urls_dictionary.has_key('alink_url'):
                urls_list.append(alink_url)
                urls_dictionary[alink_url] = True

for i in range(URLS_NUM):
    print urls_list[i]
    analyse_page(urls_list[i])







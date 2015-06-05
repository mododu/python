# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
from bs4 import BeautifulSoup

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
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    content = get_page(url, headers)
    soup = BeautifulSoup(content)
    #print soup.prettify().encode('utf-8','ignore')
    #print type(content)
    #write_file('test2.html', content)
    div_content = soup.find_all('div', class_='content')
    div_content_str = ''
    for item in div_content:
        div_content_str += item.prettify()
    #print div_content_str.encode('utf-8', 'ignore')
    write_file('test2.html', div_content_str.encode('gbk', 'ignore'))

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

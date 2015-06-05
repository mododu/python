__author__ = 'Xanadu'

import urllib
import urllib2
import re

class Spider:

    def __init__(self):
        self.siteURL =  'http://mm.taobao.com/json/request_top_list.htm'

    def get_page(self, page_index):
        url = self.siteURL + '?page=' + str(page_index)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def get_content(self, page_index):
        page = self.get_page( page_index )
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern, page)

        for item in items:
            print item
spider = Spider()
spider.get_content(1)
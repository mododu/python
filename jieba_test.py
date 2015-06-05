# -*- coding: UTF-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba
strings = '²İÄàÂí'
seg_list = jieba.cut(strings)
tmp = ' '.join(seg_list)
tmp2 = tmp.decode('utf-8').encode('gb2312')
print tmp2#type(tmp2)
print strings

# -*- coding: utf8 -*-
# coding: utf8

import sys  
reload(sys)
sys.setdefaultencoding('utf8')  
import urllib
from bs4 import BeautifulSoup
url = 'https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E7%AF%80%E6%97%A5%E8%88%87%E6%AD%B2%E6%99%82%E5%88%97%E8%A1%A8'
response = urllib.urlopen(url)
html = response.read()
sp = BeautifulSoup(html) 



tbls=sp.find_all('table',attrs={ 'class' : 'wikitable' })
trs=sp.find_all('tr',attrs={ 'style' : 'background:#efefef' })
print trs
tbls=unicode(tbls)

encoded = tbls
msg = encoded.decode('utf8')
#print msg


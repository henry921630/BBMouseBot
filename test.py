# -*- coding: utf8 -*-
# coding: utf8
import re
import sys
from time  import sleep 
import csv
import linecache
reload(sys)
sys.setdefaultencoding('utf8') 
command="嗶鼠倒數1分鐘又3秒"

csvfile = file('msghistory2.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
]
data2 = [
    ('小芳', '18', '789456')
    ]
writer.writerows(data)
writer.writerows(data2)

csvfile.close()
# -*- coding: utf8 -*-
# coding: utf8
import sys  
reload(sys)
sys.setdefaultencoding('utf8') 
from time import sleep
import re
command=u"吃了晚餐999元"


#s=re.search("",command).group()
#s= command[command.index("用")+1:(command.index("了")-1)]
amount=re.search('\D(\d{1,4})\D',command).group(1)
#print (s)
print("amount:" + amount)

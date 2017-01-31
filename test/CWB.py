# -*- coding: utf8 -*-
# coding: utf8
import urllib
import json
import pprint
# url="http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-061?locationName=大安區&sort=time"
# # print(urllib.quote(str(command)))
# response = urllib.urlopen(url)
# data = json.loads(response.read())

import urllib2
req = urllib2.Request("http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-061?locationName=大安區&sort=time")
req.add_header('Authorization', 'CWB-8CF7A304-AB2A-4E73-9F18-CE6C77F9E86D')
resp = urllib2.urlopen(req)
#content = json.loads(resp.read())
print resp
content = json.loads(resp.read())
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(content)
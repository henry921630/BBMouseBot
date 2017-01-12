# -*- coding: utf8 -*-
# coding: utf8
import urllib
import json
import pprint

command="三重石二鍋在哪裡？"

url="https://maps.googleapis.com//maps/api/place/textsearch/json?query="+urllib.quote(str(command))+"&key=AIzaSyB2OR9CaYyS8rObfyGKUB4cBul0meWu3k8&language=zh-TW"
# print(urllib.quote(str(command)))
response = urllib.urlopen(url)
data = json.loads(response.read())
#print (data)
#BBMresponse_str[1]="https://www.google.com.tw/maps/place/"+data['results'][0]['name'].replace(" ","+")

detailurl="https://maps.googleapis.com/maps/api/place/details/json?placeid={placeid}&key=AIzaSyB2OR9CaYyS8rObfyGKUB4cBul0meWu3k8&language=zh-TW".format(placeid=data['results'][0]['place_id'])
detailresponse=urllib.urlopen(detailurl)
detaildata=json.loads(detailresponse.read())
#BBMresponse_str[1]=detaildata['result']['url']
print(detaildata['result']['url'])
print (type(detaildata))
#print (data['results'])
#BBMresponse_str[2]=(data['results'][0]['formatted_address'])
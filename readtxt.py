# -*- coding: utf8 -*-
# coding: utf8

import re
#列出待辦事項
command="新增待辦事項 這是第二條"
command="完成了第一項"
# f = open('ToDoList.txt','r')
# TDL=f.read().split(",")
# print(TDL)
# TDLmsg=""
# TDLorder=0
# for i in TDL:
# 	TDLmsg=TDLmsg +str(TDLorder)+":"+ i+"\n"
# 	TDLorder+=1
# print (TDLmsg)
# f.close


#更新待辦事項
def updateToDoList(command):
	f = open('ToDoList.txt','rb')
	
	TDL=f.read().split(",")
	f.close
	TDLmsg=""
	TDLorder=0
	for i in TDL:
		TDLmsg=TDLmsg +str(TDLorder)+":"+ i+"\n"
		TDLorder+=1

	if "完成" in command:
		numberinchinese=["一","二","三","四","五","六","七","八","九","十","十一","十二","十三","十四","十五","十六","十七","十八","十九","二十","二十一","二十二","二十三","二十四","二十五","二十六","二十七","二十八","二十九","三十","三十一","三十二","三十三","三十四","三十五","三十六","三十七","三十八","三十九","四十","四十一","四十二","四十三","四十四","四十五","四十六","四十七","四十八","四十九","五十","五十一","五十二","五十三","五十四","五十五","五十六","五十七","五十八","五十九","六十","六十一","六十二","六十三","六十四","六十五","六十六","六十七","六十八","六十九","七十","七十一","七十二","七十三","七十四","七十五","七十六","七十七","七十八","七十九","八十","八十一","八十二","八十三","八十四","八十五","八十六","八十七","八十八","八十九","九十","九十一","九十二","九十三","九十四","九十五","九十六","九十七","九十八","九十九","一百"] 
		#因為十二和十一都包含了"十" 所以應該倒著檢測
		numberinarabic=range(1,101)
		for i in range(20):#假設待辦事項不會超過二十項
			if numberinchinese[9-i] in command:
				command=command.replace(numberinchinese[9-i],str(numberinarabic[9-i]))
				# command=command.replace("一","1")
		ordercompleted=int(re.search('\D(\d{1,2})',command).group(1))
		
		del TDL[ordercompleted]


		TDLline=""
		for i in range(len(TDL)):
			
			TDLline=TDLline+TDL[i]+","
			
		f = open('ToDoList.txt','wb')
		#為了消除結尾逗號，少取一格
		f.write(TDLline[:-1])
		print("TDLline")
		print(TDLline[:-1])		

	elif "新增" in command:
		f = open('ToDoList.txt','rb')
		command=command.replace("新增","").replace("待辦事項","").replace(" ","")
		
		TDL.append(command)
		TDLline=""
		for i in range(len(TDL)):
			
			TDLline=TDLline+TDL[i]+","
			
		f = open('ToDoList.txt','wb')
		#為了消除結尾逗號，少取一格
		f.write(TDLline[:-1])
		print("TDLline")
		print(TDLline[:-1])


updateToDoList(command)
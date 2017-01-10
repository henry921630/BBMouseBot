# -*- coding: utf8 -*-
# coding: utf8
import time
import re
def getTimeValue(command):
    hour=min=sec=0

    if("晚上" in command or "下午" in command or "夜晚" in command):
        AMPM="PM"
    elif("清早" in command or "早上" in command or "上午" in command):
        AMPM="AM"
    else:
        AMPM="PM" #感覺下午和晚上的行程會比較多，所以預設是PM (好像邏輯有點薄弱XD)
    numberinchinesee=["一","二","三","四","五","六","七","八","九","十","十一","十二","十三","十四","十五","十六","十七","十八","十九","二十","二十一","二十二","二十三","二十四","二十五","二十六","二十七","二十八","二十九","三十","三十一","三十二","三十三","三十四","三十五","三十六","三十七","三十八","三十九","四十","四十一","四十二","四十三","四十四","四十五","四十六","四十七","四十八","四十九","五十","五十一","五十二","五十三","五十四","五十五","五十六","五十七","五十八","五十九","六十","六十一","六十二","六十三","六十四","六十五","六十六","六十七","六十八","六十九","七十","七十一","七十二","七十三","七十四","七十五","七十六","七十七","七十八","七十九","八十","八十一","八十二","八十三","八十四","八十五","八十六","八十七","八十八","八十九","九十","九十一","九十二","九十三","九十四","九十五","九十六","九十七","九十八","九十九","一百"
] #因為十二和十一都包含了"十" 所以應該倒著檢測
    numberinarabic=range(1,101)
    for num in range(0,12): #測小時，只要一到十二就好
        # print(num)
        # print(numberinchinesee[11-num])
        if (numberinchinesee[11-num] in command[command.index("點")-3:command.index("點")]):
            command=command.replace(numberinchinesee[11-num],str(numberinarabic[11-num]))
    for num in range(0,60): #測分鐘，要一到六十
        print (numberinchinesee[59-num])
        print (command.index("點"))
        if (numberinchinesee[59-num] in command[command.index("點"):command.index("點")+4]):
            print ("有")
            command=command.replace(numberinchinesee[59-num],str(numberinarabic[59-num]))
    
    TimeValueHour=int(re.search('\D(\d{1,2})',command[command.index("點")-3:command.index("點")]).group(1))+12*(AMPM=="PM")
    print ("_"+command)
    #TimeValueMin=int(re.search('\D(\d{1,2})',command[command.index("點")+1:command.index("點")+4]).group(1))
    #print (TimeValueHour)
    #print(AccountingSentenceAnalysis_get_date(command))
    TimeValueforGoogleCalendar= AccountingSentenceAnalysis_get_date(command) + "T" + "{hour:0>2}:{min:0>2}:{sec:0>2}".format(hour=TimeValueHour,min=min,sec=sec)+"+08:00"
    print (TimeValueforGoogleCalendar)
    return TimeValueforGoogleCalendar

def isVaildDate(date):
        try:
            if ":" in date:
                time.strptime(date, "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(date, "%Y%m%d")
            return True
        except:
            return False 


def getseperatepoint(command):
    seperatepoint=-1
    try:
        seperatepoint=command.index(" ")
    except:        
        pass
        #print ("no this seperatepoint")
    try:
        seperatepoint=command.index(",")
    except:        
        pass
        #print ("no this seperatepoint")
    try:
        seperatepoint=command.index("，")
    except:        
        pass
        #print ("no this seperatepoint")
    try:
        seperatepoint=command.index(":")
    except:        
        pass
        #print ("no this seperatepoint")
    try:
        seperatepoint=command.index("：")
    except:
        pass
        #print ("no this seperatepoint")
    return seperatepoint


def AccountingSentenceAnalysis_get_date(command):
    command=command[getseperatepoint(command)+1:]
    try:
        RegularExpressDate_8digit=(re.search('[0-9]{8}', command)).group()
    except:
        RegularExpressDate_8digit=""
       #print ("無八碼")

    if "今天" in command or "today"  in command or "now"  in command or "剛剛"  in command  or "剛才"  in command or "我剛"  in command:
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60))                  #八小時乘上六十分鐘乘上六十秒
    elif "昨" in command or "yesterday"  in command  :
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60 -60*60*24))                  #八小時乘上六十分鐘乘上六十秒 再減一天回到昨天
    elif "前天" in command or "before yesterday"  in command  :
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60 -2*60*60*24))                  #八小時乘上六十分鐘乘上六十秒 再減二天回到前天

    elif "明天" in command or "tomorrow"  in command  :
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60 +60*60*24))                  #八小時乘上六十分鐘乘上六十秒 再加一天進到明天
    elif "後天" in command or "after tomorrow"  in command  :
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60 +2*60*60*24))                  #八小時乘上六十分鐘乘上六十秒 再加兩天進到後天

    elif "禮拜" in command or "周"  in command  or "週"  in command:
        if "上"  in command:        
            w=command.count("上")
        elif "下" in command:
            w=-command.count("下")
        else:
            w=0
        if "禮拜一" in command or "週一" in command or "周一" in command:
            wd=1
        elif "禮拜二" in command or "週二" in command or "周二" in command:
            wd=2
        elif "禮拜三" in command or "週三" in command or "周三" in command:
            wd=3
        elif "禮拜四" in command or "週四" in command or "周四" in command:
            wd=4
        elif "禮拜五" in command or "週五" in command or "周五" in command:
            wd=5
        elif "禮拜六" in command or "週六" in command or "周六" in command:
            wd=6
        elif "禮拜日" in command or "週日" in command or "周日" in command:
            wd=7
        else:
            pass
        #待做 先回到本週一，再減去週數，再加到指定weekday
        dt=datetime.datetime.fromtimestamp(time.mktime(time.gmtime())+60*60*8) #調整八小時時區後的現在時間(datetime)
        thisMonday=dt-datetime.timedelta(days=datetime.date.today().weekday())        
        lastMonday=thisMonday-datetime.timedelta(7*w)
        lastSomeday=lastMonday+ datetime.timedelta(wd-1)
        timetuple=lastSomeday.timetuple()
        accDate=time.strftime("%Y-%m-%d", timetuple)          
    elif isVaildDate( RegularExpressDate_8digit) == True:
        accDate=RegularExpressDate_8digit[:4] + "-" + RegularExpressDate_8digit[4:6] +"-" +RegularExpressDate_8digit[6:]
    else:
        #accDate="日期格式記錯了"
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60))                  #如果偵測不到日期就預設為今天

    return accDate

command="提醒我晚上七點十五要洗衣服"
getTimeValue(command)
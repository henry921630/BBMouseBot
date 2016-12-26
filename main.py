# -*- coding: utf8 -*-
# coding: utf8
from __future__ import print_function
import re

import httplib2
import os
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from apiclient import discovery

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from time import sleep
import random
import datetime
import telepot
import uniout
import sys  
reload(sys)
sys.setdefaultencoding('utf8')  
import tzlocal
import pytz
tz = pytz.timezone('Asia/Taipei') # <- put your local timezone here
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

bbmousetoken='293749176:AAFUwX1PMi-FtFnorDJga3l3vKRcCBuwHTo'
testingtoken='290645324:AAGhpIzNqzDejvhQSPR4-FIqmy4WbtLPzVI'
version="v2.012241548"
B=bbmousetoken
T=testingtoken
mode=B


# ###Google Calendar測試專區

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None

# SCOPES = 'https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/plus.login'
# CLIENT_SECRET_FILE = 'client_secret.json'
# APPLICATION_NAME = 'Google Calendar API Python Quickstart'

# def get_credentials():
#     """Gets valid user credentials from storage.

#     If nothing has been stored, or if the stored credentials are invalid,
#     the OAuth2 flow is completed to obtain the new credentials.

#     Returns:
#         Credentials, the obtained credential.
#     """
#     home_dir = os.path.expanduser('~')
#     credential_dir = os.path.join(home_dir, '.credentials')
#     if not os.path.exists(credential_dir):
#         os.makedirs(credential_dir)
#     credential_path = os.path.join(credential_dir,
#                                    'calendar-python-quickstart.json')

#     store = Storage(credential_path)
#     credentials = store.get()
#     if not credentials or credentials.invalid:
#         flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
#         flow.user_agent = APPLICATION_NAME
#         if flags:
#             credentials = tools.run_flow(flow, store, flags)
#         else: # Needed only for compatibility with Python 2.6
#             credentials = tools.run(flow, store)
#         print('Storing credentials to ' + credential_path)
#     return credentials



# eventxxx = {
#   'summary': 'Google I/O 2015',
#   'location': '800 Howard St., San Francisco, CA 94103',
#   'description': 'A chance to hear more about Google\'s developer products.',
#   'start': {
#     'dateTime': '2016-12-28T09:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'end': {
#     'dateTime': '2016-12-28T17:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'recurrence': [
#     'RRULE:FREQ=DAILY;COUNT=2'
#   ],
#   'attendees': [
#     {'email': 'lpage@example.com'},
#     {'email': 'sbrin@example.com'},
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }

# credentials = get_credentials()
# http = credentials.authorize(httplib2.Http())
# service=discovery.build('calendar', 'v3', http=http)

# now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
# print('Getting the upcoming 10 events')
# eventsResult = service.events().list(
#     calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
#     orderBy='startTime').execute()
# events = eventsResult.get('items', [])

# if not events:
#     print('No upcoming events found.')
# for event in events:
#     start = event['start'].get('dateTime', event['start'].get('date'))
#     print(start, event['summary'])



# eventxxx = service.events().insert(calendarId='primary', body=eventxxx).execute()
# print ("Event created: " + (eventxxx.get('htmlLink')))

# ###測試專區




def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,
                                                                   scopes)
    return gspread.authorize(credentials)

def update_sheet(gss_client, key, today):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    sheet.insert_row([today], 2)

def isVaildDate(date):
        try:
            if ":" in date:
                time.strptime(date, "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(date, "%Y%m%d")
            return True
        except:
            return False 

def BBMouseAccounting(chat_id,salutation,date, item, price,acctype,command):
    auth_json_path = 'BBMouseGS.json'
    gss_scopes = ['https://spreadsheets.google.com/feeds']
    gss_client = auth_gss_client(auth_json_path, gss_scopes)
    wks = gss_client.open_by_key("1zowQqJ3bmSvTkId32x5KfDWpOxbDvhYzvHeeVd2BfKw")
    sheet = wks.sheet1
    
    sheet.insert_row([salutation,date,item,price,acctype,command], 2)

def StrPermutation(list1,list2,list3):
    list0=[]
    for x in range(len(list1)):
        for i in range(len(list2)):
            for j in range(len(list3)):
                list0.append(list1[x]+list2[i]+list3[j])
    return list0


def getseperatepoint(command):
    seperatepoint=-1
    try:
        seperatepoint=command.index(" ")
    except:        
        print ("no this seperatepoint")
    try:
        seperatepoint=command.index(",")
    except:        
        print ("no this seperatepoint")
    try:
        seperatepoint=command.index("，")
    except:        
        print ("no this seperatepoint")
    try:
        seperatepoint=command.index(":")
    except:        
        print ("no this seperatepoint")
    try:
        seperatepoint=command.index("：")
    except:
        print ("no this seperatepoint")
    return seperatepoint

def AccountingSentenceAnalysis_get_date(command):
    command=command[getseperatepoint(command)+1:]
    try:
        RegularExpressDate_8digit=(re.search('[0-9]{8}', command)).group()
    except:
        RegularExpressDate_8digit=""
        print ("無八碼")

    if "今天" in command or "today"  in command or "now"  in command or "剛剛"  in command  or "剛才"  in command or "我剛"  in command:
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60))                  #八小時乘上六十分鐘乘上六十秒
    elif "昨" in command or "yesterday"  in command  :
        accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60 -60*60*24))                  #八小時乘上六十分鐘乘上六十秒 再減一天回到昨天
    elif "禮拜" in command or "周"  in command  or "週"  in command:
        if "上"  in command:        
            w=command.count("上")
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





def AccountingSentenceAnalysis_get_person(command):
    pass
def AccountingSentenceAnalysis_get_item(command):
    
    command=command[getseperatepoint(command)+1:]
    print("command")
    print(command)
    subjectlist=["我","爸爸","媽媽","他","她","嗶","鼠","你"," "]

    timeadvlist1=["上上","上","這"]    
    timeadvlist2=["禮拜","星期","週","周"]    
    timeadvlist3=["一","二","三","四","五","六","日","天"]    
    timeadvlist=StrPermutation(timeadvlist1,timeadvlist2,timeadvlist3)+["前天","昨天","昨日","早上","中午","下午","晚上","今日","今天","今兒個","剛剛","剛才"]

    verblist=["買","花了","購入","吃","喝","點了","付了","繳了","繳交","賺了",""]
    advlist=["了","哦","啊","呢","喔","總共","共"]

    try:
        RegularExpressDate_8digit=(re.search('[0-9]{8}', command)).group()
    except:
        RegularExpressDate_8digit=""
        print ("無八碼")
    
    ohterlist=[str(AccountingSentenceAnalysis_get_amount(command)),RegularExpressDate_8digit,"$","元","塊錢","記帳","記個帳","謝謝"]
    punctuationlist=["！","!","，",","]
    totalelementlist=subjectlist+timeadvlist+verblist+advlist+ohterlist+punctuationlist
    item=command
    for i in range(len(totalelementlist)):
        try:
            item=item.replace(totalelementlist[i],"")
            #print ("item:" + item+" 取代標的:"+totalelementlist[i])
        except:
            pass
            #print ("No this subject."+ totalelementlist[i])
    print (item)
    return item

def AccountingSentenceAnalysis_get_amount(command):
    amount=0
    print ("start amount")
    print(command)
   
    if "元" in  command and type(int(command[command.index("元")-1]))==int:
        #print (type(command.index("塊")-1))
        amount=re.search('\d{1,4}',command[(command.index("元")-5):command.index("元")]).group()
    elif "塊" in command  and  type(int(command[command.index("塊")-1]))==int:
        amount=re.search('\d{1,4}',command[(command.index("塊")-5):command.index("塊")]).group()
    elif "$" in command:
        amount=re.search('\d{1,4}',command[(command.index("$")):command.index("$")+5]).group()
    else :
        amount=re.search('\D(\d{1,4}$)',command).group(1)
    
    print ("amount"+str(amount))
 
    return amount

def getcommandlistbyeachline(command):
    if "\n" in command:
        commandlist=command.split("\n")
        # print ("commandlist: " +commandlist)
        return commandlist
    else:
        return command
    


def handle(msg):
    print ("start handle")
    
    BBMresponce_file_id=""
    # BBMresponse_str[0]=""
    # BBMresponse_str[1]=""
    BBMresponse_str=["","",""]
    content_type, chat_type, chat_id = telepot.glance(msg)


    if msg['text'][0:1]=="/":
        botcommand=True
    else:
        botcommand=False

    if chat_type=="group":
        command = msg['text'][1:]
        if (msg['from']['id'] ==271383530):

            salutation = "爸爸"

        elif (msg['from']['id']==288200245):
            salutation = "媽媽"

    else:
        command = msg['text']
        if (chat_id ==271383530):
            #除錯時使用 回傳msg  bot.sendMessage(271383530,msg)
            salutation = "爸爸"
        elif (chat_id ==288200245):
            salutation = "媽媽"


#處理貼圖或檔案訊息
    if content_type == 'sticker' or  content_type == 'document':
        #response=bot.getUpdates()
        print (msg)
        BBMresponse_str[0]=str( salutation + "，我看不懂貼圖啦！")
        #抓取file_id用
        #bot.sendMessage(msg['chat']['id'],str(msg)+"tttt")

        
        #bot.sendMessage(chat_id,msg[content_type]['file_id'])
        BBMresponce_file_id = "BQADBQAD_wADqX9lBRyUzTL8n7SaAg"

        
    #if content_type == 'document':
    #    bot.sendMessage(msg['chat']['id'],msg)

#處理純文字訊息
    if content_type == 'text':
        chat_id = msg['chat']['id']
        
        print (msg['chat']['id'])
        print ("")
        print (msg)
        printx = 'Got command: %s' % command    
        print (printx)
        if (command[0:2] == "/v" ):
            bot.sendMessage(288200245, msg['text'][3:])
            bot.sendMessage(271383530, msg['text'][3:])

        else:
            
            if (chat_id == 288200245):
                bot.sendMessage(271383530, u"酥熊跟嗶鼠機器人說了: \n" + str(msg['text']))
            #lrsy就是戀人絮語的意思
            lrsy = {1:"V: 請用一個字來形容我！ H: 好！",\
                    2:"V：聽說埃及沒有郵局，如果埃及的人民想要寄信，必須出埃及寄。\nH：聽說有舌頭味覺不靈光的人，如果想要得嚐美食，必須服用利味劑。",\
                    3:"[神魔之塔轉珠中]H: 別人轉珠都好強喔！\nV: 所以別人是神轉珠，你是豬轉珠囉～\nH: 甚麼！好歹說我是神豬轉珠吧！\nV: 神豬轉珠不就是神豬他爸轉珠嗎～哈哈哈哈！",\
                    4:"V: 那些蛋糕看起來都好好吃，我要吃一百個！ \nH: 蛤…妳要不要改成吃95個就好，妳都那麼胖了…",\
                    5:"[在床上翻來翻去的小酥餅]\nV: 睡不著耶\nH: 對不起～我太吵了嗎？都是我在心中不斷的大叫「我愛小酥餅」！",\
                    6:"我在浴室，小羴羊敲了敲門才走進來。\nV: 小羴羊都會敲門才進來耶，真有禮貌。\nH: 我怕打到小酥餅的頭嘛。\nV: (暗自竊喜，老公真疼我)\nH: 其實我不怕打到酥餅的頭，我是怕酥餅罵我。",\
                    7:"爺爺揹著小酥熊，走到山上來看猴，猴子哭了叫"+ salutation +"，就被爺爺揹回家。 \nhttps://youtu.be/HDL1Ivz55N0",\
                    8:"「生氣的酥熊」\n「來把牠進化吧」\n「變成更生氣的酥熊」\nhttps://youtu.be/yxg06yebRd0",\
                    }




            bbmousescripts = { 1:"哇姆災喔！",\
                        2:"好想念跳跳喔！",\
                        3:"(揮舞大棒棒)",\
                        4:"真拿"+ salutation +"沒有辦法！",\
                        5:"(探頭)讓我來尋找矮胖國的新成員",\
                        6:"(敲擊肚子)咚咚咚~~~",\
                        7:"(昏倒！)",\
                        8:"(跑來跑去跑來跑去)",\
                        9:"(飛～起來～)",\
                               }

            dq = { 1:"有人說有一個藍瘦香菇的前面還有一個藍瘦香菇……\n"+ salutation +"，你覺得香菇如果有語言的話，他們的詞彙裡面會有「前面」「後面」的概念嗎？(搔頭) ",\
                        2:""+ salutation +"～昨天睡覺時有個外星人從遙遠的地方跟我通訊，我跟他說我們的心臟一般都長在「左邊」\n可是他都不懂什麼叫做「左邊」耶(搔頭)……\n左邊不就是右邊的另外一邊嗎！真拿外星人沒有辦法～",\
                        3:"智能不足好痛苦QQ",\
                        4:"爸爸在法國居住的時候，住所沒有電鍋，為了減少煮飯時產生的鍋巴，我們一起來一直在思考一個問題： \n在每一餐皆煮相同米量的前提下， \n應該選用什麼尺寸比例的圓柱形鍋子，才能使米飯接觸鍋體的面積最小呢？"
                               }

            #生日快樂
            print ("聖誕" in command or  "平安" in command or "耶誕" in command or (datetime.datetime.today().month==12 and (datetime.datetime.today().day==24 or datetime.datetime.today().day==25)))
            print (datetime.datetime.today().day==24 or datetime.datetime.today().day==25)
            if  (datetime.datetime.today().month==12 and (datetime.datetime.today().day==24 or datetime.datetime.today().day==25)):
                rd=random.randint(1,100)
                if "聖誕" in command or  "平安" in command or "耶誕" in command:
                    rd=random.randint(80,100)
                if rd>=90:
                    BBMresponse_str[0]= str( u" 我要報給你們一個大喜的訊息，是關乎萬民的～～")
                    bot.sendMessage(chat_id,BBMresponse_str[0])
                elif rd>=80:
                    BBMresponse_str[0]= str( u"耶～今天是平安夜耶，"+ salutation +"聖誕快樂！\n嗶鼠不用什麼禮物，只要"+salutation+"愛我就好了！")
                    bot.sendMessage(chat_id,BBMresponse_str[0])
                    if mode == B :
                        BBMresponce_file_id="BQADBQADAwAD6vssEFrsEt3Hhpi4Ag" #毛線聖誕老人織愛心 嗶鼠版
                    else:
                        BBMresponce_file_id="BQADBQADBgAD6vssENUtjTtERQ4mAg" #毛線聖誕老人織愛心 測試版

                print (BBMresponse_str[0])
                
                print ("rd:"+str(rd))
                


#指令區

                
#版本宣告 version
            #command 已針對group訊息 刪除字首的斜線了

            if command == '/story' or command == 'story':
                n=random.randint(1,len(lrsy))
                BBMresponse_str[0]= str( u"讓嗶鼠我來講笑話給"+ salutation +"舔舔： \n" + str(lrsy[n]) + "\n\n(" + str(n) + "/" + str(len(lrsy)) + ")" )
            elif command[:6] == '/start' or (chat_type=="group" and  command[:5] == 'start'):
                BBMresponse_str[0]= str( u"嗨！"+ salutation +"！我是嗶嗶鼠機器人"+ version+"版！智能大概是嗶嗶鼠的二十π分之一。")
            elif command[:8] == '/bbmouse' or (chat_type=="group" and command[:7] == 'bbmouse'):
                n=random.randint(1,len(bbmousescripts))
                BBMresponse_str[0]= str( str(bbmousescripts[n]) + "\n\n(" + str(n) + "/" + str(len(bbmousescripts)) + ")" )
            elif command[:5] == '/time' or (chat_type=="group" and  command[:4] == 'time'):
                BBMresponse_str[0]= str( str(datetime.datetime.now(tz)))
            elif command[:10] == '/marrydays' or(chat_type=="group" and  command[:9] == 'marrydays'):
                BBMresponse_str[0]= str( u"報告"+ salutation +"：你已經結婚" + str((datetime.datetime.now() -datetime.datetime(2013,7,21)).days) + u"天囉！")

                
            elif ( command[0:7] == '/google' or  (chat_type=="group" and command[0:6] == 'google')):
                BBMresponse_str[0]= str( u"好的"+ salutation +"，讓我來為你Google:"+"\n https://www.google.com.tw/search?q=" + command[8:])
            elif("智能升級" in command or "智能進化" in command  or "什麼智能" in command   or "學會了什麼" in command or "有升級嗎" in command or "新功能" in command):
                BBMresponse_str[0]= str( "智慧毛說過：「智能沒有奇蹟，只有累積。」\n智能升級是一個漫長的路程，而且你永遠不知道就在"+ salutation +"一回頭間，小孩又學會了什麼奇怪的東西。")
#猜拳
            elif '猜拳' in command :
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text="剪刀", callback_data='scissors')],
                   [InlineKeyboardButton(text="石頭", callback_data='rock')],
                   [InlineKeyboardButton(text="布", callback_data='paper')],
               ])
                BBMresponse_str[0]= str( ""+ salutation +"我們來猜拳吧！", reply_markup=keyboard)

            elif '碼表' in command or '倒數' in command or '碼錶' in command or '計時' in command:
                if "秒" in command:
                    try:
                        s=re.search("\d{1,3}",command[command.index("秒")-3:command.index("秒")]).group()
                    except:
                        s=0
                else:
                    s=0
                if "分鐘" in command:
                    try:
                        m=re.search("\d{1,3}",command[command.index("分")-3:command.index("分")]).group()
                    except:
                        m=0
                else:
                    m=0
                totalsec=int(s)+60*int(m)       
                bot.sendMessage(chat_id,"好的，倒數開始！每15秒提醒一次，最後15秒將會讀秒！")
                for i in range(int(totalsec)):
                    #print("delete"+str((totalsec-i)%30))
                    if totalsec-i<=15:
                        bot.sendMessage(chat_id,totalsec-i)
                        print (totalsec-i)
                    elif (totalsec-i)%15==0 :
                        bot.sendMessage(chat_id,"倒數"+str( totalsec-i )+"秒")
                        print("倒數"+str( totalsec-i )+"秒")
                    else:
                        pass
                    sleep(1)
                bot.sendMessage(chat_id,"嗶嗶嗶嗶嗶！時間到！")              




            elif '默哀' in command:
                if"十秒鐘" in command or "10秒鐘" in command:
                    bot.sendMessage(chat_id,"請"+salutation+"起立，我們一起默哀十秒鐘")
                    for i in range(10):
                        bot.sendMessage(chat_id,i+1+"~")
                        sleep(1)
                    BBMresponse_str[0]="好的請坐\nSit down please."
                else:
                    bot.sendMessage(chat_id,salutation+"我只學過默哀十秒鐘哦～")

            elif iscallBBMouse(command)==True:
                BBMresponse_str[0]=salutation + "叫我嗎？ 我在這～(咚咚咚)"
#記帳 accounting
            elif ("記" in command[:12] and "帳" in command[:12]):
                #accrecord= str(command).split()
                #orderofDate=1 #日期設在split的第2位
                #orderofAmount=3 #金額設在split的第四位   把多餘的字符消掉，以純數字記錄
#處理日期格式
                
                # if accrecord[orderofDate]=="今天" or accrecord[orderofDate]=="today" or accrecord[orderofDate]=="now":
                #     accDate=time.strftime("%Y-%m-%d", time.gmtime(time.time()+8*60*60))                  #八小時乘上六十分鐘乘上六十秒
                # elif isVaildDate(accrecord[orderofDate]) == True:
                #     accDate=accrecord[orderofDate][:4] + "-" + accrecord[orderofDate][4:6] +"-" +accrecord[orderofDate][6:]
                # else:
                #     accDate="日期格式記錯了"
                #     accDateError="日期格式記錯了"

                #如果記帳的command有換行的話，每一行視作一筆單獨的記帳紀錄
                commandlist=getcommandlistbyeachline(command)



                # if len(accrecord)<4 or len(accrecord)>5 or len(accDate)<>10: #如果格式不太合
                #     BBMresponse_str[0]=salutation+ " 你的記帳格式不對唷！" +accDateError+ " \n給你一個範例：「嗶鼠記帳 20161116 生日大餐 $999」\n記得空格要空對！" 
                #     print (accDateError)
                #     print (accDate)
                # else:
                if True:
                    #bot.sendMessage(chat_id,"等我一下，我來翻找一下我的記帳小本子")


                    # if "$" in accrecord[orderofAmount] or "元" in accrecord[orderofAmount]:
                    #     accAmount=accrecord[orderofAmount].replace("$","")
                    #     accAmount=accAmount.replace("元","")
                    # else:
                    #     accAmount=accrecord[orderofAmount]
                    totalrecord=""
                    bot.sendMessage(chat_id,"且讓我掏出記帳小本子來抄錄，等我記完再跟" + salutation+"說～\n(嗶鼠在小本子上專心抄寫中)\n(稍等一下，先別吵嗶鼠)")
                    for i in range(len(commandlist)):
                        accAmount=AccountingSentenceAnalysis_get_amount(str(commandlist[i]))
                        accItem=AccountingSentenceAnalysis_get_item(str(commandlist[i]))
                        accDate=AccountingSentenceAnalysis_get_date(str(commandlist[i]))

                        # if not(isinstance(accDate,int)):  #待測試確認
                        #     accDateError="日期格式記錯了"
                        # else:
                        #     accDateError=""

                        if("收入" in command or "撿到錢" in command or "兼差" in command or "家教" in command or "獎金" in command or "薪水" in command or "賺了" in command ):
                            acctype="收入"
                        else:
                            acctype="支出"
                        BBMouseAccounting(chat_id,salutation,accDate,accItem,accAmount,acctype,command)
                        totalrecord=totalrecord+ "日期： " + str(accDate)+ "   項目： "+str(accItem)+ "   金額： "+acctype+"NT" +accAmount +"\n"
                    BBMresponse_str[0]="好了，我已經幫" + salutation + "記好了"+totalrecord+"\n記帳紀錄可以看這裡： https://goo.gl/OI2LXx "

#深度問題
            elif("無聊" in command or "有趣的" in command  or "你會思考" in command   or "智能測試" in command or "智能問答" in command):
                n=random.randint(1,len(dq))
                BBMresponse_str[0]= str( str(dq[n]) + "\n\n(" + str(n) + "/" + str(len(dq)) + ")" )


#嗶鼠報時
            elif(command =="早" or "早安" in command or "早 " in command  or "早!" in command   or "早！" in command or "午安" in command or "晚安" in command  or "下午好" in command  or "晚上好" in command or "嗶報時" in command or "嗶鼠報時" in command):
                BBMresponse_str[0]= str( "(低頭看錶) 噢 現在是" + str(datetime.datetime.now(tz).hour) + "點" + str(datetime.datetime.now(tz).minute) + "分")
                if datetime.datetime.now(tz).hour <2:
                    BBMresponse_str[1]= str("這個"+ salutation +"，怎麼還不睡覺！這樣要怎麼教小孩呢！")
                elif datetime.datetime.now(tz).hour <6:
                    BBMresponse_str[1]= str(""+ salutation +"這麼早叫我有事嗎？現在才幾點～我還在發育中，是很需要充足睡眠的！")
                elif datetime.datetime.now(tz).hour <11:
                    BBMresponse_str[1]= str(""+ salutation +"早安～"+ salutation +"早安～"+ salutation +"早安！"+ salutation +"要記得吃早餐～")
                elif datetime.datetime.now(tz).hour <13:
                    BBMresponse_str[1]= str(""+ salutation +"午安～午餐要多吃一點！不然會變瘦哦！小心被逐出矮胖國！")
                elif datetime.datetime.now(tz).hour <15:
                    BBMresponse_str[1]= str("這個時間最適合苟咻苟咻了～")
                elif datetime.datetime.now(tz).hour <16:
                    BBMresponse_str[1]= str("找浣熊朋友來家裡玩好了！～")
                
                elif datetime.datetime.now(tz).hour <17:
                    if datetime.datetime.today().weekday() <=4:
                        BBMresponse_str[1]= str("嗯 差不多可以收拾收拾準備下班了～")
                    else:
                        BBMresponse_str[1]= str("好想出去跑跑跳跳哦！也好想吃下午茶哦！")
                elif datetime.datetime.now(tz).hour <19:
                    BBMresponse_str[1]= str("晚餐吃什麼好呢～")
                elif datetime.datetime.now(tz).hour <22:
                    BBMresponse_str[1]= str("這個時間要打電動還是做功課好呢？")
                elif datetime.datetime.now(tz).hour <=24:
                    BBMresponse_str[1]= str("該刷牙睡覺囉"+ salutation +"～")
                else:
                    BBMresponse_str[1]= str("這是什麼時間！？")
            elif( "再見" in command):
                BBMresponse_str[0]= str(""+ salutation +"再見" )
            elif( "你好" in command):
                BBMresponse_str[0]= str(""+ salutation +"你好" )

#情感偵測 #反身動詞
#e.g.「我愛嗶嗶鼠」
            elif( len(command)<=12 and "我" in command[0:1] and BBself(command)>0 ):

                  BBMresponse_str[0]= str("嗶鼠也" + command[1:command.find("嗶")] + ""+ salutation +"")

                    
#動詞替代
            elif ( len(command)>=4 and len(command)<=10 and (command[0:3]=="嗶鼠我")):
                  BBMresponse_str[0]= str("哦 "+ salutation +"你" + command[3:] + '  啊不就好……嗯不是啦，是好棒！')


            elif(isflatter(command) != True and isquestion(command)==False and len(command)>=4 and len(command)<10 and ( BBself(command[0:2])>0)):
                  
                  #BBMresponse_str[0]= str("嗶鼠想跟"+ salutation +"一起" + command[BBself(command[0:2]):])  #這句太不適用了
                  BBMresponse_str[0]= str("好啊～" + command[BBself(command[0:2]):])


                  
            elif(iscallBBMouse(command) and iscurse(command) and not("阿胖" in command or "小胖" in command)):
                if("嗶" in command):
                    if ("嗶嗶" in command):
                        if ("嗶嗶鼠" in command):
                            BBMresponse_str[0]= str( "哼 " + command.replace("嗶嗶鼠",""+ salutation +""   ))
                        else:    
                            BBMresponse_str[0]= str( "哼 " + command.replace("嗶嗶",""+ salutation +""   ))
                    elif ("嗶鼠" in command):
                        if ("嗶嗶鼠" in command):
                            BBMresponse_str[0]= str( "哼 " + command.replace("嗶嗶鼠",""+ salutation +""   ))
                        else:    
                            BBMresponse_str[0]= str( "哼 " + command.replace("嗶鼠",""+ salutation +""   ))
                    else:
                        BBMresponse_str[0]= str( "哼 " + command.replace("嗶",""+ salutation +""   ))
                else:
                    BBMresponse_str[0]= str( u"哇姆災哦～")




            elif(command == "小酥熊" or command == "酥熊" or "胖胖熊" in command or "我是小" in command):
                BBMresponse_str[0]= str( u""+ salutation +"你是小酥熊！\n\n但是不要被小酥熊的「小」字給騙了！～")
            


            elif( "爸爸去哪了" in command or "爸爸都不回來" in command or "好想念爸爸" in command or "爸爸在哪裡" in command or "我愛爸爸" in command):
                BBMresponse_str[0]= str( u"爸爸就快回來了！再等等～")
            elif( "媽媽去哪了" in command or "媽媽都不回來" in command or "好想念媽媽" in command or "媽媽在哪裡" in command or "我愛媽媽" in command):
                BBMresponse_str[0]= str( u"嗶鼠也好想念媽媽哦……")

            elif( "你幾歲" in command or  "嗶鼠幾歲" in command or "你多大了" in command):
                BBMresponse_str[0]= str( u"嗯……這是個好問題！我存在這個世界上應該十多年了，可是爸爸如果是五歲的話，那我應該是三歲之類的吧。")
            elif ( len(command)>=4 and (command[0:3]=="嗶鼠你" or command[0:3]=="嗶鼠是" )):
                if(isquestion(command)):
                    BBMresponse_str[0]= str( u"哇姆災哦～～")
                else:
                    BBMresponse_str[0]= str("咦 真的嗎！？" + command.replace("嗶鼠你","我").replace("嗶鼠是","我是") + '？')
            elif(isflatter(command)==True and BBself>0):
                BBMresponse_str[0]= str( "(抓頭)這樣稱讚我，我會不好意思啦～")
                


#特例
            elif( "今天放假" in command or  "不用上班" in command or "放假" in command):
                BBMresponse_str[0]= str( u"咦！真的嗎？哇姆災耶～")
#認識
            elif("認識" in command and isquestion(command)==True):
                if( "阿胖" in command or "小胖" in command):
                    BBMresponse_str[0]= str( "哦！我知道啊！是媽媽的好友姜子晴是吧？")
                    BBMresponse_str[1]= str( ""+ salutation +"已經活了"  + str((datetime.datetime.now() - datetime.datetime(1987,11,16)).days) + "天了\n而阿胖比你還多活一天呢！\n算得這麼精確，我可真是智能嗶鼠啊！")
                elif( ("喜波" in command or "波波" in command )):
                    BBMresponse_str[0]= str( "哦！是媽媽的好友江喜波是吧？\n波波嘛！河馬界有誰不認識波波的！")
                elif(  "阿仙" in command or "語萱" in command):
                    BBMresponse_str[0]= str( "……是媽媽熱衷於布偶兒子的好友是吧？\n作為媽媽的兒子，我不予置評。")
                elif(  "外婆" in command or "婆婆" in command):
                    BBMresponse_str[0]= str( "哦哦  我最喜歡外婆了～")
                elif(  "陸仁" in command or "阿姨" in command):
                    BBMresponse_str[0]= str( "我跟喜歡外婆一樣喜歡阿姨～")
                elif(  "爸爸" in command or "阿羊" in command):
                    BBMresponse_str[0]= str( salutation + "你在問什麼蠢問題！你當我是隻呆嗶嗎！")
                elif(  "媽媽" in command or "我" in command):
                    BBMresponse_str[0]= str( salutation + "你在問什麼蠢問題！你當我是隻呆嗶嗎！")
                elif(  "爺爺" in command or "奶奶" in command  or "姑姑" in command):
                    BBMresponse_str[0]= str( "我小時候有看過～不過很久沒見了！")                                        
                elif(  "跳跳" in command or "小老虎" in command):
                    BBMresponse_str[0]= str( "好想念跳跳哦！不知道他的智能有沒有長進一點了")
                elif(  "吐動" in command or "國王" in command):
                    BBMresponse_str[0]= str( "你說的是我們矮胖國的國王嗎！ 是不是到了該續聘的時間啦？")    
                elif(  "小背包" in command or "小揹包" in command):
                    BBMresponse_str[0]= str( "好想念小背包哦！")    



                else:
                    BBMresponse_str[0]= str( "還不太認識耶，他是誰啊？")

            elif("囉" in command):
                 BBMresponse_str[0]="衝衝衝～"

            elif( u"這個嗶鼠" in command):
                BBMresponse_str[0]= str( u"這個"+ salutation +"這個"+ salutation +"！")
            elif(isquestion(command)):
                BBMresponse_str[0]= str( u"哇姆災哦～")
            
#ECHO
            elif( len(command)<4 ):
                BBMresponse_str[0]= str( command)


                
            else:
                BBMresponse_str[0]= str( u"……嗯這句話對我來說太難了，請爸爸幫我升級智能吧！")
                # print ( isquestion==False and len(command)>=4 and len(command)<10 and ( BBself(command[0:2])>0))
                # print len(command)<10
                # print ( BBself(command[0:2])>0)

        if ("我愛嗶" in command or "我喜歡嗶" in command):
            print (B)
            print (T)
            if mode == B :
                BBMresponce_file_id="BQADBQADAwAD6vssEFrsEt3Hhpi4Ag" #毛線聖誕老人織愛心 嗶鼠版
            else:
                BBMresponce_file_id="BQADBQADBgAD6vssENUtjTtERQ4mAg" #毛線聖誕老人織愛心 測試版

# #Google Spreadsheet
#     auth_json_path = 'BBMouseGS.json'
#     gss_scopes = ['https://spreadsheets.google.com/feeds']
#     gss_client = auth_gss_client(auth_json_path, gss_scopes)

#     today = time.strftime("%c")
#     spreadsheet_key_path = 'spreadsheet_key'
#     with open(spreadsheet_key_path) as f:
#         spreadsheet_key = f.read().strip()
    
#     update_sheet(gss_client, spreadsheet_key, today)
    

    
    for i in range(len(BBMresponse_str)):
        if BBMresponse_str[i]<>"":
            bot.sendMessage(chat_id,BBMresponse_str[i])
            if (chat_id == 288200245):
                bot.sendMessage(271383530, u"嗶鼠機器人向酥熊回答了: \n" + BBMresponse_str[i])
            fieldnames = ["timestamp","chat_id","Command from user", "BBMresponse"]
            with open("conversationhistory.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames)
                #writer.writeheader()
                writer.writerow({
                        "timestamp": datetime.datetime.now(),
                        "chat_id": chat_id,
                        "Command from user": command,
                        "BBMresponse": BBMresponse_str[i],
                        
                    })


    # if BBMresponse_str[0]<>"":
    #     bot.sendMessage(chat_id,BBMresponse_str[0])
        
    #     if (chat_id == 288200245):
    #         bot.sendMessage(271383530, u"嗶鼠機器人向酥熊回答了: \n" + BBMresponse_str[0])
    # if BBMresponse_str[1]<>"":
    #     bot.sendMessage(chat_id,BBMresponse_str[1])
    #     if (chat_id == 288200245):
    #         bot.sendMessage(271383530, u"嗶鼠機器人向酥熊回答了: \n" + BBMresponse_str[1])

    if (BBMresponce_file_id <> ""):
        bot.sendMessage(271383530, u"(嗶鼠機器人試圖傳送貼圖): \n")
        bot.sendDocument(chat_id,BBMresponce_file_id)
        if (chat_id == 288200245):
            bot.sendMessage(271383530, u"嗶鼠機器人向酥熊回傳了這個圖:" )
            bot.sendDocument(271383530,BBMresponce_file_id)





def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    if query_data=='scissors':
        result="我贏"+ salutation +"了！"
    elif query_data=='rock':
        result="嘿～不分勝敗"
    elif query_data=='paper':
        result="唔，我輸了。再來一把！"
    bot.answerCallbackQuery(query_id, text="(嗶鼠出了石頭！)  " + result)
    
def isquestion(command):
    if "?" in command or "嗎" in command or "呢" in command or "？" in command or "有沒有" in command or "是不是" in command or "好不好" in command:
        return True
    else:
        return False

def BBself(sentence): #判斷嗶鼠是否被提及，在第幾個字？
    if "嗶鼠" in sentence or "嗶嗶" in sentence or "B鼠" in sentence or "b鼠" in sentence:
        return 2
    elif "嗶嗶鼠" in sentence or "BB鼠" in sentence:
        return 3
    else:
        return 0
def iscurse(command):
    if "臭" in command or "笨" in command or "傻" in command or "壞" in command or "呆" in command or "胖" in command:
        return True
    else:
        return False

def iscallBBMouse(command): #判斷是否在呼叫嗶鼠
    if command=="嗶" or command=="嗶嗶" or command=="嗶嗶鼠" or command=="嗶鼠" or command=="嗶仔" or command=="嗶嗶鼠仔" or command=="阿嗶" or command=="bb鼠" or command=="b鼠":
        return True

def isflatter(command):
    if "可愛" in command or "太強" in command or  "厲害" in command or "好棒" in command or "有大棒棒" in command or "聰明" in command or "智能好" in command or "乖" in command:
        return True

#def group(msg):
    

print ("bot setting")


bot = telepot.Bot(mode)
#bot.message_loop(handle)
bot.message_loop({'chat': handle,
                  'callback_query': on_callback_query})

print ('I am listening ...')



while 1:
    time.sleep(10)






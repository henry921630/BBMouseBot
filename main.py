# -*- coding: utf8 -*-
# coding: utf8


import time
import random

import datetime

import telepot

import sys  
reload(sys)
sys.setdefaultencoding('utf8')  
#print "test"
#Set TimeZone
import tzlocal
import pytz
tz = pytz.timezone('Asia/Taipei') # <- put your local timezone here
#now = datetime.now(tz) # the current time in your local timezone

bbmousetoken= '293749176:AAFUwX1PMi-FtFnorDJga3l3vKRcCBuwHTo'
testingtoken='290645324:AAGBYFAnK6yCusuijM3plvDfhnxk3rgIlsg'

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        chat_id = msg['chat']['id']
        command = msg['text']
        print msg['chat']['id']
        print 'Got command: %s' % command    

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
                    7:"爺爺揹著小酥熊，走到山上來看猴，猴子哭了叫媽媽，就被爺爺揹回家。 \nhttps://youtu.be/HDL1Ivz55N0",\
                    8:"「生氣的酥熊」\n「來把牠進化吧」\n「變成更生氣的酥熊」\nhttps://youtu.be/yxg06yebRd0",\
                    }




            bbmousescripts = { 1:"哇姆災喔！",\
                        2:"好想念跳跳喔！",\
                        3:"(揮舞大棒棒)",\
                        4:"真拿媽媽沒有辦法！",\
                        5:"(探頭)讓我來尋找矮胖國的新成員",\
                        6:"(敲擊肚子)咚咚咚~~~",\
                        7:"(昏倒！)",\
                        8:"(跑來跑去跑來跑去)",\
                        9:"(飛～起來～)",\
                               }



            #生日快樂

            if command != "/start" and datetime.datetime.today().month==11 and datetime.datetime.today().day==16:
                bot.sendMessage(chat_id, u"耶～今天是媽媽生日，生日快樂！")
                


#指令區
            if command == '/story':
                n=random.randint(1,len(lrsy))
                bot.sendMessage(chat_id, u"讓嗶鼠我來講笑話給媽媽舔舔： \n" + str(lrsy[n]) + "\n\n(" + str(n) + "/" + str(len(lrsy)) + ")" )
            #版本宣告 version
            elif command == '/start':
                bot.sendMessage(chat_id, u"嗨！媽媽！我是嗶嗶鼠機器人v1121.1453版！智能大概是嗶嗶鼠的二十π分之一。")
            elif command == '/bbmouse':
                n=random.randint(1,len(bbmousescripts))
                bot.sendMessage(chat_id, str(bbmousescripts[n]) + "\n\n(" + str(n) + "/" + str(len(bbmousescripts)) + ")" )
            elif command == '/time':
                bot.sendMessage(chat_id, str(datetime.datetime.now(tz)))
            elif command == '/marrydays':
                bot.sendMessage(chat_id, u"報告媽媽：你已經結婚" + str((datetime.datetime.now(tz) -datetime.datetime(2013,7,21)).days) + u"天囉！")
            elif ( command[0:7] == '/google'):
                bot.sendMessage(chat_id, u"好的媽媽，讓我來為你Google:"+"\n https://www.google.com.tw/search?q=" + command[8:])



            elif(command =="早" or "早安" in command or "早 " in command  or "早!" in command   or "早！" in command or "午安" in command or "晚安" in command  or "下午好" in command  or "晚上好" in command or "報時" in command):
                bot.sendMessage(chat_id, "(低頭看錶) 噢 現在是" + str(datetime.datetime.now(tz).hour) + "點" + str(datetime.datetime.now(tz).minute) + "分")
                if datetime.datetime.now(tz).hour <2:
                    bot.sendMessage(chat_id,"這個媽媽，怎麼還不睡覺！這樣要怎麼教小孩呢！")
                elif datetime.datetime.now(tz).hour <6:
                    bot.sendMessage(chat_id,"媽媽這麼早叫我有事嗎？現在才幾點～我還在發育中，是很需要充足睡眠的！")
                elif datetime.datetime.now(tz).hour <11:
                    bot.sendMessage(chat_id,"媽媽早安～媽媽早安～媽媽早安！媽媽要記得吃早餐～")
                elif datetime.datetime.now(tz).hour <13:
                    bot.sendMessage(chat_id,"媽媽午安～午餐要多吃一點！不然會變瘦哦！小心被逐出矮胖國！")
                elif datetime.datetime.now(tz).hour <15:
                    bot.sendMessage(chat_id,"這個時間最適合苟咻苟咻了～")                    
                elif datetime.datetime.now(tz).hour <17:
                    if datetime.datetime.today().weekday() <=4:
                        bot.sendMessage(chat_id,"嗯 差不多可以收拾收拾準備下班了～")
                    else:
                        bot.sendMessage(chat_id,"好想出去跑跑跳跳哦！也好想吃下午茶哦！")
                elif datetime.datetime.now(tz).hour <19:
                    bot.sendMessage(chat_id,"晚餐吃什麼好呢～")
                elif datetime.datetime.now(tz).hour <22:
                    bot.sendMessage(chat_id,"這個時間要打電動還是做功課好呢？")
                elif datetime.datetime.now(tz).hour <=24:
                    bot.sendMessage(chat_id,"該刷牙睡覺囉媽媽～")
                else:
                    bot.sendMessage(chat_id,"這是什麼時間！？")
                    
            elif( "臭" in command or "笨" in command or "傻" in command or "胖" in command):
                if("嗶" in command):
                    if ("嗶嗶" in command):
                        bot.sendMessage(chat_id, "哼 " + command.replace("嗶嗶","媽媽"   ))
                    if ("嗶鼠" in command):
                        if ("嗶嗶鼠" in command):
                            bot.sendMessage(chat_id, "哼 " + command.replace("嗶嗶鼠","媽媽"   ))
                        else:    
                            bot.sendMessage(chat_id, "哼 " + command.replace("嗶鼠","媽媽"   ))
                    else:
                        bot.sendMessage(chat_id, "哼 " + command.replace("嗶","媽媽"   ))

            elif( "爸爸去哪了" in command or "爸爸都不回來" in command or "好想念爸爸" in command or "爸爸在哪裡" in command):
                bot.sendMessage(chat_id, u"這個媽媽這個媽媽！")
                
            elif( "你幾歲" in command or  "嗶鼠幾歲" in command or "你多大了" in command):
                bot.sendMessage(chat_id, u"嗯……這是個好問題！我存在這個世界上應該十多年了，可是爸爸如果是五歲的話，那我應該是三歲之類的吧。")
            elif( "太強" in command or  "厲害" in command or "好棒" in command or "有大棒棒" in command or "聰明" in command or "智能好" in command):
                bot.sendMessage(chat_id, "(抓頭)這樣稱讚我，我會不好意思啦～")
                
            elif( u"這個" in command):
                bot.sendMessage(chat_id, u"這個媽媽這個媽媽！")
            elif( u"嗎" in command or  u"呢" in command or u"呢" in command):
                bot.sendMessage(chat_id, u"哇姆災哦～")
            

            elif( len(command)<4 ):
                bot.sendMessage(chat_id, command)
            elif( "今天放假" in command or  "不用上班" in command or "放假" in command):
                bot.sendMessage(chat_id, u"咦！真的嗎？哇姆災耶～")                
            else:
                bot.sendMessage(chat_id, u"……嗯這句話對我來說太難了，你還是直接找爸爸好了！ https://telegram.me/yhlhenry")
            
print "bot setting"        
bot = telepot.Bot(bbmousetoken)
bot.message_loop(handle)
print 'I am listening ...'



while 1:
    time.sleep(10)

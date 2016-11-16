# -*- coding: utf8 -*-
# coding: utf8

import time
import random
import datetime
import telepot
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  


def handle(msg):
        
    chat_id = msg['chat']['id']
    command = msg['text']

    if command[0:2] == "/v":
        'bot.sendMessage(288200245, msg['text'][4:])
        bot.sendMessage(271383530, msg['text'][4:])
    else:
        lrsy = {1:"V: 請用一個字來形容我！ H: 好！",\
                2:"V：聽說埃及沒有郵局，如果埃及的人民想要寄信，必須出埃及寄。\nH：聽說有舌頭味覺不靈光的人，如果想要得嚐美食，必須服用利味劑。",\
                3:"[神魔之塔轉珠中]H: 別人轉珠都好強喔！\nV: 所以別人是神轉珠，你是豬轉珠囉～\nH: 甚麼！好歹說我是神豬轉珠吧！\nV: 神豬轉珠不就是神豬他爸轉珠嗎～哈哈哈哈！",\
                4:"V: 那些蛋糕看起來都好好吃，我要吃一百個！ \nH: 蛤…妳要不要改成吃95個就好，妳都那麼胖了…",\
                5:"[在床上翻來翻去的小酥餅]\nV: 睡不著耶\nH: 對不起～我太吵了嗎？都是我在心中不斷的大叫「我愛小酥餅」！",\
                6:"我在浴室，小羴羊敲了敲門才走進來。\nV: 小羴羊都會敲門才進來耶，真有禮貌。\nH: 我怕打到小酥餅的頭嘛。\nV: (暗自竊喜，老公真疼我)\nH: 其實我不怕打到酥餅的頭，我是怕酥餅罵我。"}

        bbmouse = { 1:"哇姆災喔！",\
                    2:"好想念跳跳喔！",\
                    3:"(揮舞大棒棒)",\
                    4:"真拿媽媽沒有辦法！",\
                    5:"(探頭)讓我來尋找矮胖國的新成員",\
                    6:"(敲擊肚子)咚咚咚~~~"}



        #生日快樂

        if command != "/start" and datetime.datetime.today().month==11 and datetime.datetime.today().day==16:
            bot.sendMessage(chat_id, u"耶～今天是媽媽生日，生日快樂！")
            

        print msg['chat']['id']
        print 'Got command: %s' % command

        if command == '/story':
            bot.sendMessage(chat_id, u"讓嗶鼠我來講笑話給媽媽舔舔： \n" + str(lrsy[random.randint(1,6)]))
        elif command == '/start':
            bot.sendMessage(chat_id, u"嗨！媽媽！我是嗶嗶鼠機器人。不是嗶嗶鼠，是嗶嗶鼠機器人！智能大概是嗶嗶鼠的二十π分之一。")
        elif command == '/bbmouse':
            bot.sendMessage(chat_id, str(bbmouse[random.randint(1,6)]))
        elif command == '/time':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
        elif command == '/marrydays':
            bot.sendMessage(chat_id, u"報告媽媽：你已經結婚" + str((datetime.datetime.now() -datetime.datetime(2013,7,21)).days) + u"天囉！")
        elif ( command[0:7] == '/google'):
            bot.sendMessage(chat_id, u"好的媽媽，讓我來為你Google:"+"\n https://www.google.com.tw/search?q=" + command[8:])
        elif( u"這個" in command):
            bot.sendMessage(chat_id, u"哇姆災哦～")
        elif( u"嗎" in command):
            bot.sendMessage(chat_id, u"哇姆災哦～")
        elif( u"呢" in command):
            bot.sendMessage(chat_id, u"哇姆災哦～")
        elif( u"?" in command):
            bot.sendMessage(chat_id, u"哇姆災哦～")
        elif( len(command)<5 ):
            bot.sendMessage(chat_id, command)
        
        else:
            bot.sendMessage(chat_id, u"……嗯這句話對我來說太難了，你還是直接找爸爸好了！ https://telegram.me/yhlhenry")
        
        
bot = telepot.Bot('293749176:AAFUwX1PMi-FtFnorDJga3l3vKRcCBuwHTo')
bot.message_loop(handle)
print 'I am listening ...'



while 1:
    time.sleep(10)

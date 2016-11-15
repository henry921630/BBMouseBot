# -*- coding: utf8 -*-
# coding: utf8

import time
import random
import datetime
import telepot


def handle(msg):
        
    chat_id = msg['chat']['id']
    command = msg['text']



    #生日快樂

    if comman != "/start" and datetime.datetime.today().month==11 and datetime.datetime.today().day==16:
        bot.sendMessage(chat_id, u"耶～今天是媽媽生日，生日快樂！")
        

    print msg['chat']['id']
    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/start':
        bot.sendMessage(chat_id, u"嗨！媽媽！我是嗶嗶鼠機器人。不是嗶嗶鼠，是嗶嗶鼠機器人！智能大概是嗶嗶鼠的二十π分之一。")
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

    
    else:
        bot.sendMessage(chat_id, u"……嗯這句話對我來說太難了，你還是直接找爸爸好了！ https://telegram.me/yhlhenry")
    
    
bot = telepot.Bot('293749176:AAFUwX1PMi-FtFnorDJga3l3vKRcCBuwHTo')
bot.message_loop(handle)
print 'I am listening ...'



while 1:
    time.sleep(10)

# -*- coding: utf8 -*-
# coding: utf8


import GetFileID




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


from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

bbmousetoken='293749176:AAFUwX1PMi-FtFnorDJga3l3vKRcCBuwHTo'
testingtoken='290645324:AAGBYFAnK6yCusuijM3plvDfhnxk3rgIlsg'

def handle(msg):
    print u"start handle"
    
    BBMresponce_file_id=""
    BBMresponse_str1=""
    BBMresponse_str2=""
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
            bot.sendMessage(271383530,msg)
            salutation = "爸爸"
        elif (chat_id ==288200245):
            salutation = "媽媽    "


#處理貼圖或檔案訊息
    if content_type == 'sticker' or  content_type == 'document':
        response=bot.getUpdates()
        print msg
        BBMresponse_str1=str( salutation + "，我看不懂貼圖啦！")
        #抓取file_id用
        #bot.sendMessage(msg['chat']['id'],str(msg)+"tttt")

        
        #bot.sendMessage(chat_id,msg[content_type]['file_id'])
        BBMresponce_file_id = "BQADBQAD_wADqX9lBRyUzTL8n7SaAg"

        
    #if content_type == 'document':
    #    bot.sendMessage(msg['chat']['id'],msg)

#處理純文字訊息
    if content_type == 'text':
        chat_id = msg['chat']['id']
        
        print msg['chat']['id']
        print ""
        print msg
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

            if command != "/start" and datetime.datetime.today().month==11 and datetime.datetime.today().day==16:
                BBMresponse_str1= str( u"耶～今天是"+ salutation +"生日，生日快樂！")
                


#指令區

                
#版本宣告 version
            

            if command == '/story' or command == 'story':
                n=random.randint(1,len(lrsy))
                BBMresponse_str1= str( u"讓嗶鼠我來講笑話給"+ salutation +"舔舔： \n" + str(lrsy[n]) + "\n\n(" + str(n) + "/" + str(len(lrsy)) + ")" )
            elif command[:6] == '/start' or (chat_type=="group" and  command[:5] == 'start'):
                BBMresponse_str1= str( u"嗨！"+ salutation +"！我是嗶嗶鼠機器人v1211.1745版！智能大概是嗶嗶鼠的二十π分之一。")
            elif command[:8] == '/bbmouse' or (chat_type=="group" and command[:7] == 'bbmouse'):
                n=random.randint(1,len(bbmousescripts))
                BBMresponse_str1= str( str(bbmousescripts[n]) + "\n\n(" + str(n) + "/" + str(len(bbmousescripts)) + ")" )
            elif command[:5] == '/time' or (chat_type=="group" and  command[:4] == 'time'):
                BBMresponse_str1= str( str(datetime.datetime.now(tz)))
            elif command[:10] == '/marrydays' or(chat_type=="group" and  command[:9] == 'marrydays'):
                BBMresponse_str1= str( u"報告"+ salutation +"：你已經結婚" + str((datetime.datetime.now() -datetime.datetime(2013,7,21)).days) + u"天囉！")

                
            elif ( command[0:7] == '/google' or  (chat_type=="group" and command[0:6] == 'google')):
                BBMresponse_str1= str( u"好的"+ salutation +"，讓我來為你Google:"+"\n https://www.google.com.tw/search?q=" + command[8:])
            elif("智能升級" in command or "智能進化" in command  or "什麼智能" in command   or "學會了什麼" in command or "有升級嗎" in command or "新功能" in command):
                BBMresponse_str1= str( "智慧毛說過：「智能沒有奇蹟，只有累積。」\n智能升級是一個漫長的路程，而且你永遠不知道就在"+ salutation +"一回頭間，小孩又學會了什麼奇怪的東西。")
#猜拳
            elif '猜拳' in command :
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text="剪刀", callback_data='scissors')],
                   [InlineKeyboardButton(text="石頭", callback_data='rock')],
                   [InlineKeyboardButton(text="布", callback_data='paper')],
               ])
                BBMresponse_str1= str( ""+ salutation +"我們來猜拳吧！", reply_markup=keyboard)




#深度問題
            elif("無聊" in command or "有趣的" in command  or "你會思考" in command   or "智能測試" in command or "智能問答" in command):
                n=random.randint(1,len(dq))
                BBMresponse_str1= str( str(dq[n]) + "\n\n(" + str(n) + "/" + str(len(dq)) + ")" )


#嗶鼠報時
            elif(command =="早" or "早安" in command or "早 " in command  or "早!" in command   or "早！" in command or "午安" in command or "晚安" in command  or "下午好" in command  or "晚上好" in command or "嗶報時" in command or "嗶鼠報時" in command):
                BBMresponse_str1= str( "(低頭看錶) 噢 現在是" + str(datetime.datetime.now(tz).hour) + "點" + str(datetime.datetime.now(tz).minute) + "分")
                if datetime.datetime.now(tz).hour <2:
                    BBMresponse_str2= str("這個"+ salutation +"，怎麼還不睡覺！這樣要怎麼教小孩呢！")
                elif datetime.datetime.now(tz).hour <6:
                    BBMresponse_str2= str(""+ salutation +"這麼早叫我有事嗎？現在才幾點～我還在發育中，是很需要充足睡眠的！")
                elif datetime.datetime.now(tz).hour <11:
                    BBMresponse_str2= str(""+ salutation +"早安～"+ salutation +"早安～"+ salutation +"早安！"+ salutation +"要記得吃早餐～")
                elif datetime.datetime.now(tz).hour <13:
                    BBMresponse_str2= str(""+ salutation +"午安～午餐要多吃一點！不然會變瘦哦！小心被逐出矮胖國！")
                elif datetime.datetime.now(tz).hour <15:
                    BBMresponse_str2= str("這個時間最適合苟咻苟咻了～")
                elif datetime.datetime.now(tz).hour <16:
                    BBMresponse_str2= str("找浣熊朋友來家裡玩好了！～")
                
                elif datetime.datetime.now(tz).hour <17:
                    if datetime.datetime.today().weekday() <=4:
                        BBMresponse_str2= str("嗯 差不多可以收拾收拾準備下班了～")
                    else:
                        BBMresponse_str2= str("好想出去跑跑跳跳哦！也好想吃下午茶哦！")
                elif datetime.datetime.now(tz).hour <19:
                    BBMresponse_str2= str("晚餐吃什麼好呢～")
                elif datetime.datetime.now(tz).hour <22:
                    BBMresponse_str2= str("這個時間要打電動還是做功課好呢？")
                elif datetime.datetime.now(tz).hour <=24:
                    BBMresponse_str2= str("該刷牙睡覺囉"+ salutation +"～")
                else:
                    BBMresponse_str2= str("這是什麼時間！？")
            elif( "再見" in command):
                BBMresponse_str1= str(""+ salutation +"再見" )
            elif( "你好" in command):
                BBMresponse_str1= str(""+ salutation +"你好" )

#情感偵測 #反身動詞
#e.g.「我愛嗶嗶鼠」
            elif( len(command)<=12 and "我" in command[0:1] and "嗶" in command ):

                  BBMresponse_str1= str("嗶鼠也" + command[1:command.find("嗶")] + ""+ salutation +"")

                    
#動詞替代
            elif ( len(command)>=4 and (command[0:3]=="嗶鼠我")):
                  BBMresponse_str1= str("哦 "+ salutation +"你" + command[3:] + '  啊不就好棒棒XD')


            elif( len(command)>=4 and len(command)<10 and (command[0:2]=="嗶鼠" or command[0:2]=="嗶嗶" )):
                  bbn=(command[0:3]=="嗶嗶鼠")
                  BBMresponse_str1= str("嗶鼠想跟"+ salutation +"一起" + command[2+bbn:])


                  
            elif( "臭" in command or "笨" in command or "傻" in command or "壞" in command or ("胖" in command and not("阿胖" in command or "小胖" in command))):
                if("嗶" in command):
                    if ("嗶嗶" in command):
                        if ("嗶嗶鼠" in command):
                            BBMresponse_str1= str( "哼 " + command.replace("嗶嗶鼠",""+ salutation +""   ))
                        else:    
                            BBMresponse_str1= str( "哼 " + command.replace("嗶嗶",""+ salutation +""   ))
                    elif ("嗶鼠" in command):
                        if ("嗶嗶鼠" in command):
                            BBMresponse_str1= str( "哼 " + command.replace("嗶嗶鼠",""+ salutation +""   ))
                        else:    
                            BBMresponse_str1= str( "哼 " + command.replace("嗶鼠",""+ salutation +""   ))
                    else:
                        BBMresponse_str1= str( "哼 " + command.replace("嗶",""+ salutation +""   ))
                else:
                    BBMresponse_str1= str( u"哇姆災哦～")




            elif(command == "小酥熊" or command == "酥熊" or "胖胖熊" in command or "我是小" in command):
                BBMresponse_str1= str( u""+ salutation +"你是小酥熊！\n\n但是不要被小酥熊的「小」字給騙了！～")
            


            elif( "爸爸去哪了" in command or "爸爸都不回來" in command or "好想念爸爸" in command or "爸爸在哪裡" in command or "我愛爸爸" in command):
                BBMresponse_str1= str( u"爸爸就快回來了！再等等～")
                
            elif( "你幾歲" in command or  "嗶鼠幾歲" in command or "你多大了" in command):
                BBMresponse_str1= str( u"嗯……這是個好問題！我存在這個世界上應該十多年了，可是爸爸如果是五歲的話，那我應該是三歲之類的吧。")
            elif ( len(command)>=4 and (command[0:3]=="嗶鼠你")):
                if( u"嗎" in command or  u"呢" in command or u"呢" in command or "吧" in command or "？" in command or "?" in command):
                    BBMresponse_str1= str( u"哇姆災哦～～")
                else:
                    BBMresponse_str1= str("咦 真的嗎！？ 我" + command[3:] + '？')
            elif( "真可愛" in command or "太強" in command or  "厲害" in command or "好棒" in command or "有大棒棒" in command or "聰明" in command or "智能好" in command or "乖" in command):
                BBMresponse_str1= str( "(抓頭)這樣稱讚我，我會不好意思啦～")
                


#特例
            elif( "今天放假" in command or  "不用上班" in command or "放假" in command):
                BBMresponse_str1= str( u"咦！真的嗎？哇姆災耶～")
            elif("認識" in command and  ("嗎" in command or "?" in command or "？" in command)):
                if( "阿胖" in command or "小胖" in command):
                    BBMresponse_str1= str( "哦！是你的好友姜子晴是吧？")
                    BBMresponse_str2= str( ""+ salutation +"已經活了"  + str((datetime.datetime.now() - datetime.datetime(1987,11,16)).days) + "天了\n而阿胖比你還多活一天呢！\n算得這麼精確，我可真是智能嗶鼠啊！")
                elif( ("喜波" in command or "波波" in command )):
                    BBMresponse_str1= str( "哦！是你的好友江喜波是吧？\n波波嘛！河馬界有誰不認識波波的！")
                elif(  "阿仙" in command or "語萱" in command):
                    BBMresponse_str1= str( "……是你熱衷於兒子的好友是吧？\n作為"+ salutation +"的兒子，我不予置評。")
                elif(  "外婆" in command or "婆婆" in command):
                    BBMresponse_str1= str( "哦哦  我最喜歡外婆了～")
                elif(  "陸仁" in command or "阿姨" in command):
                    BBMresponse_str1= str( "我跟喜歡外婆一樣喜歡阿姨～")

                    
                else:
                    BBMresponse_str1= str( "還不太認識耶，他是誰啊？")



            elif( u"這個嗶鼠" in command):
                BBMresponse_str1= str( u"這個"+ salutation +"這個"+ salutation +"！")
            elif( u"嗎" in command or  u"呢" in command or u"呢" in command or "吧" in command):
                BBMresponse_str1= str( u"哇姆災哦～")
            
#ECHO
            elif( len(command)<4 ):
                BBMresponse_str1= str( command)


                
            else:
                BBMresponse_str1= str( u"……嗯這句話對我來說太難了，請爸爸幫我升級智能吧！")

        if ("我愛嗶" in command or "我喜歡嗶" in command):
            print B
            print T
            if mode == B :
                BBMresponce_file_id="BQADBQADAwAD6vssEFrsEt3Hhpi4Ag" #毛線聖誕老人織愛心 嗶鼠版
            else:
                BBMresponce_file_id="BQADBQADBgAD6vssENUtjTtERQ4mAg" #毛線聖誕老人織愛心 測試版


    if BBMresponse_str1<>"":
        bot.sendMessage(chat_id,BBMresponse_str1)
        
        #bot.sendMessage(chat_id,msg[content_type]['file_id'])
        #bot.sendDocument(271383530,msg[content_type]['file_id'])

       #bot.sendMessage(chat_id,BBMresponce_file_id)
        #bot.sendDocument(271383530,BBMresponce_file_id)
        if (chat_id == 288200245):
            bot.sendMessage(271383530, u"嗶鼠機器人向酥熊回答了: \n" + BBMresponse_str1)
    if BBMresponse_str2<>"":
        bot.sendMessage(chat_id,BBMresponse_str2)
        if (chat_id == 288200245):
            bot.sendMessage(271383530, u"嗶鼠機器人向酥熊回答了: \n" + BBMresponse_str2)
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
    


#def group(msg):
    

print "bot setting"

B=bbmousetoken
T=testingtoken
mode=B
bot = telepot.Bot(mode)
#bot.message_loop(handle)
bot.message_loop({'chat': handle,
                  'callback_query': on_callback_query})

print 'I am listening ...'



while 1:
    time.sleep(10)

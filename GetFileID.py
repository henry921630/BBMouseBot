

def GetFileID(msg):
	import telepot

	print 'test'
	content_type, chat_type, chat_id = telepot.glance(msg)
	bot.sendMessage(chat_id,"GFID")




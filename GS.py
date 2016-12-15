import telepot

bbmousetoken='293749176:AAFUwX1PMi-FtFnorDJga3l3vKRcCBuwHTo'
bot = telepot.Bot(bbmousetoken)

def test():
	bot.sendMessage(271383530, "GS Testing")



import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
print "GS starting"

def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,
                                                                   scopes)
    return gspread.authorize(credentials)



auth_json_path = 'BBMouseGS.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

gss_client = auth_gss_client(auth_json_path, gss_scopes)


def update_sheet(gss_client, key, today, item, price):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    sheet.insert_row([today, item, price], 2)

spreadsheet_key_path = 'spreadsheet_key'

print "Cell setting"
cheapest_price="20"
cheapest_item="itemhenry"

if cheapest_price is not None:
    today = time.strftime("%c")
    with open(spreadsheet_key_path) as f:
        spreadsheet_key = f.read().strip()
    print "update starting"
    update_sheet(gss_client, spreadsheet_key, today, cheapest_item,
                 cheapest_price)

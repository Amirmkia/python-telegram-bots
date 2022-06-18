import requests
import telegram
print('connecting..')
bot = telegram.Bot(token='')
print('connected')
cap="""تخفیف های جمعه سیاه مجموعه راستاد به شرح زیر است:

کانال سیگنال و تحلیل راستاد:
یک ماهه <s>560,000 تومان</s> 500,000 تومان
سه ماهه <s>1,590,000 تومان</s> 1,000,000 تومان
یک ساله <s>6,720,000 تومان</s> 2,000,000 تومان
خرید از : smrastad.com

اشتراک Traders Hall:
یک ماهه 40 تتر
سه ماهه <strike>120 تتر</strike> 100 تتر
یک ساله <strike>480 تتر</strike> 200 تتر
خرید از @Rastad_support

💸 @RastadCo Black Friday 💸"""
class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def deleteMessage(self, chat_id, message_id):
        params = {'chat_id': chat_id, 'message_id': message_id}
        method = 'deleteMessage'
        resp = requests.post(self.api_url + method, params)
        print(resp)
        return resp

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
    def editMessageText(self, chat_id, text,message_id):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML','message_id':message_id}
        method = 'editMessageText'
        resp = requests.post(self.api_url + method, params)
        return resp

    def unbanChatMember(self,chat_id,user_id):
        params = {'chat_id':chat_id,'user_id':user_id,'only_if_banned':True}
        method = 'unbanChatMember'
        resp = requests.post(self.api_url + method, params)
        print(resp)
        return resp

    def sendVideo(self, chat_id, file_id,caption):
        params = {'chat_id': chat_id, 'video': file_id,'caption':caption}
        method = 'sendVideo'
        resp = requests.post(self.api_url + method, params)
        resp=resp.json()
        print(resp)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update
    def sendAnimation(self, chat_id, file_id,caption):
        params = {'chat_id': chat_id, 'animation': file_id,'caption':caption}
        method = 'sendAnimation'
        resp = requests.post(self.api_url + method, params)
        resp=resp.json()
        print(resp)
        return resp
    def sendPhoto(self, chat_id, file_id,caption):
        params = {'chat_id': chat_id, 'photo': file_id,'caption':caption}
        method = 'sendPhoto'
        resp = requests.post(self.api_url + method, params)
        print(resp)
        return resp

token = '1374235352:AAFDqXemFI_ZPqHxJctzmj70924f-Ah6np0' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name

# reading boardcast file
f=open('boardcast.txt')
data=f.read()
f.close()
data=data.split('\n')
print(len(data))
data=set(data)
file_id = ''
print(len(data))
for user in data:
    print('user :',user)
##    f=open('IMG_4445.MP4','rb')
##    try:
    a=magnito_bot.sendPhoto(chat_id=int(user),file_id=file_id,caption=cap)
##    except Exception as e:
##        print(e)
##        print('couldnt')
    f.close()
##    print(a)
    



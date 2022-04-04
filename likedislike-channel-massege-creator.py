from matplotlib.backend_bases import Event
from telethon import TelegramClient, Button, events 
from telethon.tl.functions.channels import DeleteMessagesRequest
import json 
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup , Update
from telethon.tl.types import PeerChannel
import random
from telethon import utils
from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
from telethon import TelegramClient

from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.functions.channels import GetParticipantsRequest

from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser
from telegram import *
from telegram.ext import *
api_id = "6507128"
api_hash = "3e7dea0acaef86a05fa54511a0f4f9c6"
CHANNEL = -1001796487584
# CHANNEL = -764117518

bot_token = "5081074973:AAEkLaJ2-WJqkmZi5DxmhluuGIZ7KPfq8S4"
i = 1
messagenumber = {
    "number" : "",
    "like" : 0,
    "dislike" : 0,
    "message" : "",
    "messageId" : "",
    "dislikenum" : "",
    "likenum": "",
    "users" : [],
    "senderId" :"",
    "usernames":[]
    }

botthon = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
bot = telegram.Bot(token=bot_token )
x = bot.get_chat_administrators("@fikelikedislike")

@botthon.on(events.NewMessage(CHANNEL))
async def my_event_handler(event):
    x = random.random()
    y = random.random()
    manegers = []
    for admin in bot.get_chat_administrators(CHANNEL):
      manegers.append(admin.user['first_name'])
    admins = ["Behrooz", "Arad" , "Amir Mohammad" , "Arash" , "A͠ ℓ ɨ 尺 e̷ ʐ α"]
    if event.message.media != None:
        for maneger in admins:
            if maneger == event.post_author:
                print("salam modiiir")
                break
        else:  
            print("modir nisti")         
            bot.deleteMessage(chat_id= CHANNEL, message_id=event.message.id)
                
    elif event.message.message :
        
            buttlikenum = messagenumber['like']
            buttdislikenum = messagenumber['dislike']
            messagenumber["senderId"] = event.post_author
            keyboard = [
            [  
                Button.inline( text = f"👍 {buttlikenum}", data = f"{y}"), 
                Button.inline(text = f"👎 {buttdislikenum}", data = f'{x}')
            ]
            ]
            messagenumber['dislikenum'] = x
            messagenumber["likenum"] = y
            global i
            messagenumber['number'] = i
            i = i + 1
            messagenumber["message"] = event.message.message
            messagenumber['messageId'] = event.id
           
            bot.deleteMessage(chat_id= CHANNEL, message_id=messagenumber['messageId'])
            await botthon.send_message(
                    event.chat_id, 
                    f"{messagenumber['message']}",  
                    buttons=keyboard
                    )
            jsonData = json.load(open('./messages.json'))
            if type(jsonData) is dict:
                jsonData = [jsonData]
            
            jsonData.append(messagenumber)

            with open('./messages.json', 'w') as outfile:
                json.dump(jsonData, outfile , indent = 4)
@botthon.on(events.CallbackQuery)
async def handler(event):

    with open('./messages.json', 'r') as f:
        data = json.load(f)
        j = 0
        
        while j < len(data):
           
            dislikenum = data[j]['dislikenum']
            likenum = data[j]['likenum']
            if event.data == bytes(f'{dislikenum}', 'utf-8'):
                if len(data[j]['users']) == 0 :
                    user = event.sender_id
                    username = event.sender.username
                    data[j]['users'].append(user)
                    data[j]['usernames'].append(username)
                    data[j]['dislike'] = int(data[j]['dislike']) + 1
                    with open('./messages.json', 'w') as file:
                     json.dump(data, file, indent=2)
                     await event.answer('نظر شما با موفقیت ذخیره شد')
                    
                    with open('./messages.json', 'r') as file:
                     data2 = json.load(file)
                     dislike = data2[j]['dislike']
                     like = data2[j]['like']
                     keyboard = [
                                  [  
                                    Button.inline( text = f"👍{like}", data = f"{likenum}"), 
                                    Button.inline(text = f"👎 {dislike}", data = f'{dislikenum}')
                                  ]
                                ]
                     await botthon.edit_message(
                        CHANNEL , int(data[j]['messageId']) + 1, str(data[j]['message']) , buttons=keyboard
                     ) 
                    file.close()
                else:
                    user = event.sender_id
                    username = event.sender.username
                    if user in data[j]['users']:
                        await event.answer('شما قبلا پاسخ داده اید' , alert = True)
                    else:
                        user = event.sender_id
                        data[j]['users'].append(user)
                        data[j]['usernames'].append(username)
                        data[j]['dislike'] = int(data[j]['dislike']) + 1
                        with open('./messages.json', 'w') as file:
                            json.dump(data, file, indent=2)
                            await event.answer('نظر شما با موفقیت ذخیره شد')
                        file.close()
                        with open('./messages.json', 'r') as file:
                         data2 = json.load(file)
                         dislike = data2[j]['dislike']
                         like = data2[j]['like']
                         keyboard = [
                                    [  
                                        Button.inline( text = f"👍{like}", data = f"{likenum}"), 
                                        Button.inline(text = f"👎 {dislike}", data = f'{dislikenum}')
                                    ]
                                    ]
                         await botthon.edit_message(
                            CHANNEL , int(data[j]['messageId']) + 1, str(data[j]['message']) , buttons=keyboard
                         )         
            if event.data == bytes(f'{likenum}', 'utf-8'):
                if len(data[j]['users']) == 0 :
                    user = event.sender_id
                    username = event.sender.username
                    data[j]['users'].append(user)
                    data[j]['usernames'].append(username)
                    data[j]['like'] = int(data[j]['like']) + 1
                    with open('./messages.json', 'w') as file:
                     json.dump(data, file, indent=2)
                     await event.answer('نظر شما با موفقیت ذخیره شد')
                    file.close()
                    with open('./messages.json', 'r') as file:
                         data2 = json.load(file)
                         dislike = data2[j]['dislike']
                         like = data2[j]['like']
                         keyboard = [
                                    [  
                                        Button.inline( text = f"👍{like}", data = f"{likenum}"), 
                                        Button.inline(text = f"👎 {dislike}", data = f'{dislikenum}')
                                    ]
                                    ]
                         await botthon.edit_message(
                            CHANNEL , int(data[j]['messageId']) + 1, str(data[j]['message']) , buttons=keyboard
                         )         
                else:
                    user = event.sender_id
                    username = event.sender.username
                    if user in data[j]['users']:
                        await event.answer('شما قبلا پاسخ داده اید' , alert = True)
                    else:
                        user = event.sender_id
                        data[j]['users'].append(user)
                        data[j]['usernames'].append(username)
                        data[j]['like'] = int(data[j]['like']) + 1
                        with open('./messages.json', 'w') as file:
                            json.dump(data, file, indent=2)
                            await event.answer('نظر شما با موفقیت ذخیره شد')
                        file.close()
                        with open('./messages.json', 'r') as file:
                         data2 = json.load(file)
                         dislike = data2[j]['dislike']
                         like = data2[j]['like']
                         keyboard = [
                                    [  
                                        Button.inline( text = f"👍{like}", data = f"{likenum}"), 
                                        Button.inline(text = f"👎 {dislike}", data = f'{dislikenum}')
                                    ]
                                    ]
                         await botthon.edit_message(
                            CHANNEL , int(data[j]['messageId']) + 1, str(data[j]['message']) , buttons=keyboard
                         )                     
            j = j + 1 
     
botthon.run_until_disconnected()
   

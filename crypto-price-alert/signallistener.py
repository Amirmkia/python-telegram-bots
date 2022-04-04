
from pyexpat.errors import messages
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon import utils
import asyncio
import logging
from telethon.events import StopPropagation
from telethon import TelegramClient
import threading
import time
import json
import datetime
import ccxt
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup , Update
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, chat
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler
)
import requests
import datetime
import time
from datetime import date
from datetime import timedelta
from telethon.tl.types import ChannelParticipantsAdmins
import ccxt
import json 
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import datetime
import time
from datetime import date
from datetime import timedelta
api_id = "6507128"
api_hash = "3e7dea0acaef86a05fa54511a0f4f9c6"
phone = ''

CHANNEL = -738934496
token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
api_key = ""
api_secret = ""
message = "hi."
client = TelegramClient('botpriceAlert', api_id, api_hash)
bot = TelegramClient('priceAlertBot', api_id, api_hash).start(bot_token=token)
group = -685093058


@client.on(events.NewMessage(CHANNEL))
async def my_event_handler(event: events.NewMessage.Event):
    splitMessage = event.message.message
    message = splitMessage.split("\n\n")
    if message[-1] == "💸 @RastadCo VIP 💸":
        dataDict = {
            "sender" : event.sender_id,
            "username" : "",
            "messageId" : event.id ,
            "name" : "",
            "enter_price" : None,
            "targets" : [],
            "stop" : "",
            "timing" : "",
            "spot" : "",
            "current_price" : "",
            "target_len" : "",
            "date" : "",
            "lev_futures": "",
            "capital" : "",
            "confirmed" : 0,
            "ts" : 0,
            "time" : str(date.today()),
            "profit" : 0 ,
            "loss" : 0,
            "date" : ""
        } 
        # print("###################################")
        sender = await event.get_sender()
        # print(sender.username)
        dataDict['username'] = sender.username
        name = message[1].replace("📶 #" , "")
        # print("name : " + str(name))
        dataDict["name"] = name
        message_enter_price = message[2].replace("📈Enter price: " , "")
        enter_price = message_enter_price.split(" 🔛 ")
        # print("enterPrice : " + str(enter_price))
        dataDict["enter_price"] = enter_price
        dataDict["spot"] = message[0]
        # print(message[3 : -4])
        targets = message[3 : -4]
        # print(targets[-1])
        # print("len : " + str(len(targets)))
        if len(targets) == 5:
            count = 0
            while count < 4:
                # print(targets[count])
                targetnumber = targets[count].split(" ")
                # print(targetnumber[2])
                dataDict["targets"].append(targetnumber[2])
                count += 1
            target5number = targets[4].split("\n")
            dataDict["targets"].append(target5number[-1])
            # print(target5number[-1])
        else:
            for target in targets:
                # print(target)
                targetnumber = target.split(" ")
                # print(targetnumber[-1])
                dataDict["targets"].append(targetnumber[-1])
        messagestop = message[-4].split (" ")
        if messagestop[1] == "Normal":
            stop = message[-4].replace("⛔️ Normal Stop Loss: " , "")
            # leverage = message[-3]
            # print( "leverage :" + leverage)
            dataDict["timing"] = "N"
        else:
            stop = message[-4].replace("⛔️ Manual Stop Loss: \nClose daily (D) candle below" , "")
            dataDict["timing"] = "D"
        timing = message[-4].split(" ")
        # print(timing[1])
        dataDict["stop"] = stop
        dataDict["target_len"] = len(dataDict["targets"])
        messagecapital = message[-3].split(" ")
        # print(messagecapital)
        if len(messagecapital) == 5 :
            character = "-"
            # print("character : " + str(messagecapital[4].find(character)))
            dash = messagecapital[4].find(character)
            if int(dash) ==True:
                levs = messagecapital[4].split("-")
                # print(levs)
                lev1 = int(levs[0])
                lev2isolated = levs[1].replace("X)" , "")
                lev2 = int(lev2isolated)
                levrage = (lev1 + lev2)/2
                # print("leverage" + str(levrage))
                dataDict['lev_futures'] = levrage
            else:
                leverage = messagecapital[4].replace("X)" , "")
                dataDict['lev_futures'] = leverage
                # print("leverage : " + str(leverage))
        capital_percent = messagecapital[1].replace("%" , "")
        # dataDict["capital"] = capital_percent
        # dataDict["date"] = str(datetime.datetime.now())
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        coin = dataDict["name"]
        exchange = dataDict["spot"].split(" ")
        exchangeCoin = exchange[0]
        method_to_call = getattr(ccxt,exchangeCoin.lower()) 
        exchange_obj = method_to_call()
        pair_price_data = exchange_obj.fetch_ticker(coin)
        closing_price = pair_price_data['close']
        # print("coin price : " + str(closing_price))
        dataDict["current_price"] = closing_price
        dataDict["enter_price_launched"] = 0            
        i = 1
        for target in dataDict["targets"]:
            dataDict[f"target{i}"] = 0
            i +=1
        # print(dataDict)
        bot_message = f"{dataDict}"
        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
        channel = "-681209528"
        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
        header = {
            "text" : bot_message
        }
        requests.post(send_text , json= header)
        with open("./Data.json" , "r") as readingDataFile:
            historyData = json.load(readingDataFile)
        with open("./Data.json" , "w") as writingDataFile:
            historyData.append(dataDict)
            json.dump(historyData , writingDataFile , indent = 6)
            
        raise events.StopPropagation

@client.on(events.NewMessage(pattern = "/cp"))
async def my_event_handler(event: events.NewMessage.Event):
    # print(event)
    # print(event.from_id.user_id)
    # print(event.reply_to_msg_id)
    with open("./Data.json" , "r") as readingSignalsFile:
        signals = json.load(readingSignalsFile)
        for signal in signals:
            if int(event.from_id.user_id) == int(signal['sender']) :
                if int(event.reply_to_msg_id) == int(signal["messageId"]):
                    # print("reply found")
                    await event.respond('سیگنال ریپلای زده با موفقیت بسته شد')
                    signal['confirmed'] = 1
                    with open("./Data.json" , "w") as writingSignalFile:
                        json.dump(signals , writingSignalFile , indent = 6)
                    break
            else:
                # print("cant find reply")
                await event.respond('سیگنالی که ریپلای زده اید پیدا نشد ، لطفا دوباره امتحان کنید')
        else:
            # print("in signal baraye shoma nist")
            await event.respond('سیگنالی که ریپلای زده اید برای شما نیست ، این آپشن فقط روی سیگنال هایی که خودتان ارسال کرده اید امکان پذیر است ،')

@client.on(events.NewMessage(pattern = "/cap"))
async def my_event_handler(event: events.NewMessage.Event):
    # print(event)
    # print(event.from_id.user_id)
    # print(event.reply_to)
    # print(event.reply_to_msg_id)
    with open('./Data.json' , "r") as readingSignalFile:
        signals = json.load(readingSignalFile)
        for signal in signals:
            if int(signal['sender']) == int(event.from_id.user_id):
                # print("I find your signal")
                if int(signal['confirmed']) == 0:
                    signal['confirmed'] = 1
                    with open("./Data.json" , "w") as writingSignalFile : 
                        json.dump(signals , writingSignalFile , indent = 6)
                    # print("succesfully closed")
                    await event.respond('سیگنال های شما با موفقیت بسته شدند در حال محاسبه ی درصد سود و زیان هرکدام...')

@client.on(events.NewMessage(pattern = "/rf"))
async def my_event_handler(event: events.NewMessage.Event):
    # print(event)
    # print(event.from_id.user_id)
    # print(event.reply_to)
    # print(event.reply_to_msg_id)
    with open("./Data.json" , "r") as readingSignalsFile:
        signals = json.load(readingSignalsFile)
        for signal in signals:
            if int(event.from_id.user_id) == int(signal['sender']) :
                if int(event.reply_to_msg_id) == int(signal["messageId"]):
                    # print("reply found")
                    await event.respond('عملیات Risk-free با موفقیت روی سیگنال انتخاب شده انجام شد')
                    firstEnterPrice = signal['enter_price'][0]
                    twoEnterPrice = signal['enter_price'][1]
                    signal['stop'] = (float(firstEnterPrice) + float(twoEnterPrice))/2
                    with open("./Data.json" , "w") as writingSignalFile:
                        json.dump(signals , writingSignalFile , indent = 6)
                    break
            else:
                # print("cant find reply")
                await event.respond('سیگنال ریپلای زده شده پیدا نشد لطفا دوباره امتحان کنید')
        else:
            # print("in signal baraye shoma nist")  
            await event.respond('این آپشن فقط روی سیگنالی که خودتان ارسال کرده اید امکان پذیر است ')              

@client.on(events.NewMessage(pattern = "/rfap"))
async def my_event_handler(event: events.NewMessage.Event):
    # print(event)
    # print(event.from_id.user_id)
    # print(event.reply_to)
    # print(event.reply_to_msg_id)
    with open('./Data.json' , "r") as readingSignalFile:
        signals = json.load(readingSignalFile)
        for signal in signals:
            if int(signal['sender']) == int(event.from_id.user_id):
                # print("I find your signal")
                if int(signal['confirmed']) == 0:
                    firstEnterPrice = signal['enter_price'][0]
                    twoEnterPrice = signal['enter_price'][1]
                    signal['stop'] = (float(firstEnterPrice) + float(twoEnterPrice))/2
                    with open("./Data.json" , "w") as writingSignalFile : 
                        json.dump(signals , writingSignalFile , indent = 6)
                    # print("succesfully changed")     
                    await event.respond('عملیات Risk-free روی تمامی سیگنال های شما با موفقیت انجام شد ')  

@client.on(events.NewMessage(pattern = "/ts"))
async def my_event_handler(event: events.NewMessage.Event):
    # print(event)
    # print(event.from_id.user_id)
    # print(event.reply_to)
    # print(event.reply_to_msg_id)
    with open("./Data.json" , "r") as readingSignalsFile:
        signals = json.load(readingSignalsFile)
        for signal in signals:
            if int(event.from_id.user_id) == int(signal['sender']) :
                if int(event.reply_to_msg_id) == int(signal["messageId"]):
                    # print("reply found")
                    signal['ts'] = 1
                    with open("./Data.json" , "w") as writingSignalFile:
                        json.dump(signals , writingSignalFile , indent = 6)
                    break
            else:
                # print("cant find reply")
                await event.respond('سیگنال ریپلای زده پیدا نشد لطفا دوباره تلاش کنید')
        else:
            # print("in signal baraye shoma nist") 
            await event.respond('این آپشن فقط روی سیگنالی که خودتان ارسال کرده اید امکان پذیر است')

@client.on(events.NewMessage(pattern = "/tsap"))
async def my_event_handler(event: events.NewMessage.Event):
    # print(event)
    # print(event.from_id.user_id)
    # print(event.reply_to)
    # print(event.reply_to_msg_id)
    with open('./Data.json' , "r") as readingSignalFile:
        signals = json.load(readingSignalFile)
        for signal in signals:
            if int(signal['sender']) == int(event.from_id.user_id):
                # print("I find your signal")
                if int(signal['confirmed']) == 0:
                    signal['ts'] = 1    
                    with open("./Data.json" , "w") as writingSignalFile : 
                        json.dump(signals , writingSignalFile , indent = 6)
                    # print("succesfully changed") 
                    await event.respond('عملیات Traling Stop  روی تمامی سیگنال های شما با موفقیت انجام شد')       

@client.on(events.NewMessage(pattern = "/Alireza"))
async def my_event_handler(event: events.NewMessage.Event):
    # print("residam behesh")
    admins = []
    async for user in client.iter_participants(CHANNEL, filter=ChannelParticipantsAdmins):
        # await event.respond(
        #     f'/{user.username}'
        #     '\n'
        #     ) 
        admins.append(user.username)
    # print(admins)
    for admin in admins :
        # print("admin : " + admin)
        with open("./Data.json" , "r") as readingSignalFile:
            signals = json.load(readingSignalFile)
        for signal in signals:
            if admin == signal["username"]:
                if signal['confirmed'] == 1:
                    await event.respond(
                        f' ADMIN : {admin}'
                        '\n'
                        f"SIGNAL : {signal['name']} ✅"
                        "\n"
                        f"DATE : {signal['date']}"
                        "\n"
                        f"ENTERPRICE : {signal['enter_price']}"
                        "\n"
                        f"TARGETS : {signal['targets']}"
                        "\n"
                        f"STOPLOSS : {signal['stop']}"
                        "\n"
                        f"TARGETS : {signal['targets']}"
                        "\n"
                        f"PROFIT : {signal['profit']}"

                    )
                if signal['confirmed'] == 0:
                    await event.respond(
                        f' ADMIN : {admin}'
                        '\n'
                        f"SIGNAL : {signal['name']} ⛔️"
                        "\n"
                        f"DATE : {signal['date']}"
                        "\n"
                        f"ENTERPRICE : {signal['enter_price']}"
                        "\n"
                        f"TARGETS : {signal['targets']}"
                        "\n"
                        f"STOPLOSS : {signal['stop']}"
                        "\n"
                        f"TARGETS : {signal['targets']}"
                        "\n"
                        f"LOSS : {signal['loss']}"
                    )
            else:
                await event.respond(
                    f"{admin}"
                    "\n"
                    "'گشاده هنوز سیگنال نداده"
                    )
 



 

     
async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
     asyncio.run(main())
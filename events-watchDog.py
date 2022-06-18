import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import pandas
import telegram
import time
import os
import tablib
from telebot import TeleBot
from telegram import Update
from telegram.ext import (Updater,
                          PicklePersistence,
                          CommandHandler,
                          CallbackQueryHandler,
                          CallbackContext,
                          ConversationHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
print("I'm ready")



def main():
    Token = ""
    bot = telegram.Bot(token= Token)
    channel = "-624744635"
    print("I'm ready in function")
    url = "https://developers.coinmarketcal.com/v1/events"
    payload = ""
    headers = {
    'x-api-key': "",
    'Accept-Encoding': "deflate, gzip",
    'Accept': "application/json"
    }
    response = requests.request("GET", url, data=payload, headers=headers)

    jsonText = json.loads(response.text)
    with open("./events.json" , "r") as readevents:
        eventlist = json.load(readevents)
        if len(eventlist):
            eventIdList = []
            for event in eventlist:
                eventIdList.append(event["id"])
            for event in jsonText['body']:
                if event["id"] in eventIdList:
                    pass
                else:
                    with open("./events.json" , "r") as readevent:
                        newevents = json.load(readevent) 
                        with open("./events.json" , "w") as writeevent:
                            datadict = {
                                "id" : "",
                                "title" : "", 
                                "coins" : [],
                                "date_event" : "",
                                "time_event" : "",
                                "categories" : [],
                                "source" : ""
                            }
                            datadict["id"] = event["id"]
                            datadict["title"] = event["title"]["en"]
                            for coinsname in event["coins"]:
                                datadict["coins"].append(coinsname["name"])
                            y = event["date_event"].split("T")
                            m = y[1].split("Z")
                            datadict["date_event"] = y[0]
                            datadict["time_event"] = m[0]
                            for categorise in event["categories"]:
                                datadict["categories"].append(categorise["name"])
                            datadict["source"] = event["source"]
                            newevents.append(datadict)
                            json.dump(newevents , writeevent , indent= 4 ) 
                            time.sleep(1)
                            # open('./events.json', 'a+').write("./events.xls")
                            # df = pandas.DataFrame(data=datadict)
                            # df = (df.T)
                            # df.to_excel('dict1.xlsx')
                            id = datadict["id"]
                            title = datadict["title"]
                            coins = datadict["coins"]
                            date_event = datadict["date_event"]
                            time_event = datadict["time_event"]
                            categories = datadict["categories"]
                            source = datadict["source"]
                            bot.send_message(
                                channel,
                                "New Project Reachead :"
                                "\n\n"
                                f"Id : {id}"
                                "\n"
                                f"title : {title}"
                                "\n"
                                f"coins : {coins}"
                                "\n"
                                f"date_event : {date_event}"
                                "\n"
                                f"time_event : {time_event}"
                                "\n"
                                f"categories : {categories}"
                                "\n"
                                f"source : {source}"
                                )
        else:
            jsonList = []
            for event in jsonText['body']:
                time.sleep(1)
                datadict = {
                    "id" : "",
                    "title" : "", 
                    "coins" : [],
                    "date_event" : "",
                    "time_event" : "",
                    "categories" : [],
                    "source" : ""
                }
                datadict["id"] = event["id"]
                datadict["title"] = event["title"]["en"]
                for coinsname in event["coins"]:
                    datadict["coins"].append(coinsname["name"])
                y = event["date_event"].split("T")
                m = y[1].split("Z")
                datadict["date_event"] = y[0]
                datadict["time_event"] = m[0]
                # bot.send_message(channel,f"{datadict}")
                time.sleep(1)
                for categorise in event["categories"]:
                    datadict["categories"].append(categorise["name"])
                datadict["source"] = event["source"]
                if type(jsonText['body'][1]) is dict :
                    jsonList.append(datadict)
                with open("./events.json" , "w") as file:
                    json.dump(jsonList , file , indent=4)
                # pandas.read_json("./events.json").to_excel("events.xlsx")
                # open('./events.json', 'w').write("./events.xls")
                time.sleep(1)
                id = datadict["id"]
                title = datadict["title"]
                coins = datadict["coins"]
                date_event = datadict["date_event"]
                time_event = datadict["time_event"]
                categories = datadict["categories"]
                source = datadict["source"]
                bot.send_message(
                    channel,
                    "New Project Reachead :"
                    "\n\n"
                    f"Id : {id}"
                    "\n"
                    f"title : {title}"
                    "\n"
                    f"coins : {coins}"
                    "\n"
                    f"date_event : {date_event}"
                    "\n"
                    f"time_event : {time_event}"
                    "\n"
                    f"categories : {categories}"
                    "\n"
                    f"source : {source}"
                    )
    

scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', hours=0.01)
scheduler.start()

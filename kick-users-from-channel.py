
from click import pass_context
from pyrogram import Client
import json
from apscheduler.schedulers.blocking import BlockingScheduler
from pyrogram.types import ChatPermissions
import requests
import time
print("im ready")
def main():
    print("run def")
    channel = -1001751666366
    app = Client(
        "my_bot",
        api_id = "6507128",
        api_hash = "",
        bot_token=""
    )
    app.start()
    members = app.get_chat_members(channel)
    memberUsername = []
    memberChatId = []
    url = "https://smrastad.com/xX983z5244/xAtp1165.php"
    websiteData = requests.get(url)
    data = eval(websiteData.text)
    urllid = "https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=get_level_users&lid=1"
    websitelidData = requests.get(urllid)
    lidData = eval(websitelidData.text)
    for member in members:
        print("member : " + member["user"]["username"])
        for id in data:
            if member["user"]["username"] == id["telegram_id"]:
                print(id["telegram_id"])
                print(id["user_id"])
                for user in lidData["response"]:
                    if id["user_id"] == user["user_id"]:
                        print(id["telegram_id"])
                        print("hast")  
                        break    
                else:
                    print(id["telegram_id"])
                    print("nist")
                break
        else:
            print(member["user"]["username"])
            print(member["user"]["id"])
            print("dar site nist")
            if member["user"]["id"] == 5193691520 or member["user"]["id"] == 382215836:
                pass
            else:
                print("==========================")
                print(member["user"]["username"])
                app.ban_chat_member(channel , int(member["user"]["id"]) , int(time.time() + 2)) 
                time.sleep(2)
                print("user banned")
        
scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', hours=0.02)
scheduler.start()


from tabnanny import check
from pytz import timezone
import telegram
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
from flask import *
import requests
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove
import os
import json
import time
import pandas as pd
import datetime
import time
import pyotp
import pyqrcode
import png
from pyqrcode import QRCode
import yagmail
import random
import base64
import datetime
qrcode = ""
newpermission , assetpay , cancelbut , packages , afterasset , aftertraderzhal , checktxidtraderhallthree , checktxidtraderhalltwo , checktxidtraderhallone , checkvipone , checkviptwo , checkvipthree , backToHome , aftervip  , AssetVip1 , AssetVip2,AssetVip3, CheckQrCodeVip1 , CheckQrCodeVip2 ,CheckQrCodeVip3 , CheckAssetVip1 ,  CheckAssetVip2,  CheckAssetVip3 , AssetTh1 , CheckQrCodeTh1 , CheckAssetTh1 , AssetTh2 ,CheckQrCodeTh2 , CheckAssetTh2 , AssetTh3 ,CheckQrCodeTh3 , CheckAssetTh3 = range(32)
bot = telegram.Bot(token="5121111058:AAHSZu6fmDKFyLWGhaCCVqd_Jl1RhVAk1NI")
def start(update: Update, context: CallbackContext) -> int:
    '''
    when user send /start this section started
    '''
    print("start run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    if len(context.args):
        param_value = context.args[0]
        if param_value == "traderhall1":
            return traderzhalonemonth(update, context)
        elif param_value == "traderhall2":
            return traderzhaltwomonth(update, context)
        elif param_value == "traderhall3":
            return traderzhalthreemonth(update, context)
        elif param_value == "vip1":
            return viponemonth(update, context)
        elif param_value == "vip2":
            return viptwomonth(update, context)
        elif param_value == "vip3" :
            return vipthreemonth(update, context)
    else:
        username = update.message.from_user['username']
        if username == None:    
            update.message.reply_text(
                "شما username telegram  ندارید ، لطفا از طریق setting telegram یک  username  برای خود بسازید و سپس روی دکمه ی 'start'در پایین بزنید"
            )
            return ConversationHandler.END
        else:
            update.message.reply_text(
            "لطفا منتظر بمانید ، در حال اتصال به سایت راستاد ..."
            )
            time.sleep(3)
            return newperm(update , context)

def newperm(update: Update , context: CallbackContext) -> int:
    '''
    this section get to the Rastad website and check user that started bot was in website or not 
    '''
    print("new perm run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    username = update.message.from_user['username']
    url = "https://smrastad.com/xX983z5244/xAtp1165.php"
    websiteData = requests.post(url)
    out_file = open("./myfile.json", "w")  
    json.dump(websiteData.json(), out_file, indent = 6) 
    out_file.close() 
    with open("./myfile.json" , "r") as readJsonFile:
        jsonFileDicts = json.load(readJsonFile)
        for jsonFiledic in jsonFileDicts:
            if jsonFiledic["telegram_id"] == username:
                reply_keyboard = [['راستاد VIP' , 'Traders Hall'] , ['لغو درخواست']]
                update.message.reply_text(
                    "اتصال شما به سایت با موفقیت انجام شد "
                    "\n"
                    "اکنون از طریق منوی پایین نحوه ی پرداخت را انتخاب کنید"
                    ,reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True) 
                )
                return packages
        else:
            reply_keyboard = [['شروع دوباره']]
            update.message.reply_text(
                    "شما در سایت راستاد اکانت ندارید و یا username telegram  که در سایت وارد کرده اید صحیح نیست ."
                  "\n"
                  "لطفا در سایت راستاد به نشانی smrastad.com وارد شوید و username telegram  خود را تصحیح کنید یا اگر اکانت ندارید بسازید ."
                  "\n"
                  "سپس روی دکمه ی 'start' در پایین بزنید"
                 , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                )
            return cancelbut

def Txid(update : Update, context: CallbackContext):
    print("txid is running")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['راستاد VIP' , 'Traders Hall'] , ['لغو درخواست']]
    update.message.reply_text(
        "لطفا پکیج مورد نظر را انتخاب کنید"
    , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return packages

def vipRastad(update : Update, context: CallbackContext):
    '''
    section vip running 
    '''
    print("vip rastad run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['یک ساله 150 دلار','سه ماهه 70 دلار' ,'یک ماهه 25 دلار'] , ['برگشت به انتخاب اشتراک ها']]
    update.message.reply_text(
        "مدت زمان اشتراک را انتخاب کنید : "
        , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return aftervip
#-------------------------------------

def howtopayth1(update : Update, context: CallbackContext):
    print("howtopayTh1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['Txid' , 'کیف پول'] , ['لغو درخواست']]
    update.message.reply_text(
        "لطفا نحوه پرداختتان را از طریق دکمه های منوی پایین انتخاب کنید"
    , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return AssetTh1

def assetTh1(update : Update, context: CallbackContext):
    print("assetTh1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    user = update.message.from_user['username']
    with open("./history.json" , "r") as historyFile:
        data = json.load(historyFile)
        # print(data)
        if len(data) > 0 :
            print("find")
            dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : ''
                }
            j = 0 
            for user in data:
                if user["username"] == update.message.from_user["username"]:
                    print("recieved")
                    update.message.reply_text(
                        "لطفا کد فرستاده شده در google authenticator  را برایمان ارسال کنید"
                    )
                    return CheckQrCodeTh1
                j = j + 1
                    
            else:
                print("cant recieved")
                with open ("./number.txt" , "r") as readingTextFile : 
                    data = readingTextFile.readlines()
                    print(data[0])
                    print(type(data[0]))
                    textdata = data[0]
                    aftertextdata = int(data[0]) + 1
                    t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                    x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    print(t.now())
                    auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                    print(auth_str)  
                    s = str(auth_str)
                    
                    url = pyqrcode.create(s)
                    url.png(f'./{user}.png', scale = 6)
                    dict = {
                        "username" : update.message.from_user['username'],
                        "packages" : [],
                        "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    }
                    with open("./history.json" , "r") as readinghistoryFile:
                        data = json.load(readinghistoryFile)
                        with open("./history.json" , "w") as writingHistoryFile:
                            data.append(dict)
                            json.dump(data , writingHistoryFile , indent = 6)
                    # with open("./number.txt" , "w") as writingTextFile : 
                    #     writingTextFile.write(str(aftertextdata))
                    update.message.reply_text(
                            "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                   "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    ) 
                    context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
                    return CheckQrCodeTh1
        else:
            print("cant find")
            print("cant recieved")
            with open ("./number.txt" , "r") as readingTextFile : 
                data = readingTextFile.readlines()
                print(data[0])
                print(type(data[0]))
                textdata = data[0]
                aftertextdata = int(data[0]) + 1
                t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                print(t.now())
                auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                print(auth_str)  
                s = str(auth_str)
                url = pyqrcode.create(s)
                url.png(f'./{user}.png', scale = 6)
                dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                }
                with open("./history.json" , "r") as readinghistoryFile:
                    data = json.load(readinghistoryFile)
                    with open("./history.json" , "w") as writingHistoryFile:
                        data.append(dict)
                        json.dump(data , writingHistoryFile , indent = 6)
                # with open("./number.txt" , "w") as writingTextFile : 
                #     writingTextFile.write(str(aftertextdata))
                update.message.reply_text(
                        "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                    "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    )
                context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
            return CheckQrCodeTh1

def checkingQRcodeTh1(update : Update, context: CallbackContext):
    print("checkingQRcodeTh1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    with open("./history.json" , "r") as historyFile : 
        data = json.load(historyFile)
        for user in data:
            if user["username"] == update.message.from_user["username"]:
                t = pyotp.TOTP(user['secret'])
                print(update.message.text)
                print(t.now())
                print(type(update.message.text))
                print(type(t.now()))
                if str(update.message.text) == str(t.now()):
                    update.message.reply_text(
                        "رمز دوم شما با موفقیت تایید شد"
                        "\n"
                        "لطفا آدرس کیف پول خود را ارسال کنید"
                    )
                    return CheckAssetTh1
                else:
                    update.message.reply_text(
                        "رمز دوم شما درست نیست لطفا دوباره وارد کنید"
                    )
            break
        else:
            print("tamaaaam")

def checkingassetTh1(update : Update, context: CallbackContext):
    print("checkingasseth1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا منتظر بمانید در حال بررسی درخواستتان..."
    )
    print(update.message.text)
    reply_keyboard = [['برگشت به محصولات']]
    url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
    websitetronData = requests.post(url)
    tronJsonData = websitetronData.json()
    tronJsonDataData = tronJsonData["data"]
    # print(tronJsonDataData)
    for asset in tronJsonDataData:
        if asset['transferFromAddress'] == update.message.text:
            print(asset)
            if asset["confirmed"] == True:
                with open ("./teronscan.json" , "r") as readingHistoryData : 
                    data = json.load(readingHistoryData)
                update.message.reply_text("آدرس کیف پولتان در تراکنش ها پیدا شد در حال بررسی مقدار واریزی...")
                for history in data:
                    if history["from_address"] == asset['transferFromAddress']:
                        print("addres ha barabar")
                        if history['transaction_id'] == asset['transactionHash']:
                            print("addrese barabar txidsh sabt shode => ban")
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "این تراکنش قبلا ثبت شده است لطفا با پشتیبانی تماس بگیرید"
                                , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                else:
                    print("barresi amount")
                    if int(asset['amount']) < 42000000 and int(asset['amount']) > 38000000 : 
                        print("amount dorost bood")
                        update.message.reply_text("مقدار واریزی درست است در حال بررسی زمان پرداخت ...")
                        time.sleep(2)
                        dateTime = str(datetime.datetime.now())
                        timeing = dateTime.split(" ")
                        hour = timeing[1].split(":")
                        print(hour[0])
                        timestampTime = asset["timestamp"]
                        tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                        timingteron = str(datetime.datetime.utcfromtimestamp(timestampTime / 1e3))
                        timingteron2 = timingteron.split(" ")
                        timingteron3 = timingteron2[1].split(":")
                        print(timingteron3[0])
                        if int(timingteron3[0]) >= int(hour[0]) - 1 and int(timingteron3[0]) <= int(hour[0]) :
                            update.message.reply_text(
                                "تراکنش شما از لحاظ زمانی نیز درست می باشد لطفا صبر کنید تا اشتراک تان فعال شود..."
                            ) 
                            tehranTime = str(tehranTime)
                            newDict = {
                                "amount" : asset["amount"],
                                "from_address" : asset["transferFromAddress"],
                                "to_address" : asset["transferToAddress"],
                                "confirmed" : asset["confirmed"],
                                "transaction_id" : asset["transactionHash"],
                                "timestamp" : tehranTime
                            }
                            with open("./teronscan.json" , "r") as teronscanreadingfile:
                                logData = json.load(teronscanreadingfile)
                            logData.append(newDict)
                            with open("./teronscan.json" , "w") as teronscanwritingfile:
                                json.dump(logData , teronscanwritingfile , indent = 6)
                            username = update.message.from_user['username']
                            with open("./myfile.json" , "r") as readJsonFile:
                                jsonFileDicts = json.load(readJsonFile)
                                historyDict = {
                                            "username" :  update.message.from_user['username'],
                                            "packages" : [],
                                            "secret" : ""
                                        }
                                print('1')
                                with open("history.json" , "r") as readinghitoryFile :
                                    historyData = json.load(readinghitoryFile)
                                    if len(historyData) > 0:
                                        print(historyData)
                                        j = 0
                                        for userHistoryData in historyData:
                                            print(userHistoryData)
                                            print('2')
                                            if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                print('3')
                                                historyDict["secret"] = userHistoryData["secret"]
                                                for i in userHistoryData["packages"]:
                                                    historyDict["packages"].append(i)
                                                historyData.remove(historyData[j])
                                                historyDict['packages'].append("اشتراک یک ماهه تریدرزهال")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as historyJsonFile :
                                                    json.dump(historyData , historyJsonFile , indent = 6)
                                                    break 
                                            j = j + 1    
                                        else:
                                            print('4')
                                            historyDict['packages'].append("اشتراک یک ماهه تریدرزهال")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                                    
                                    else:
                                        print('5')
                                        historyDict['packages'].append("اشتراک یک ماهه تریدرزهال")
                                        historyData.append(historyDict)
                                        with open("history.json" , "w") as writingHistoryFile :
                                            json.dump(historyData , writingHistoryFile , indent = 6)
                                for jsonFiledic in jsonFileDicts:
                                    if jsonFiledic["telegram_id"] == username:
                        
                                        # print(jsonFiledic["user_id"])
                                        uid = jsonFiledic["user_id"]
                                        url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=1"
                                        requests.get(url1)
                                        time.sleep(1)
                                        url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=1"
                                        # 1 time
                                        requests.get(url2)
                                        update.message.reply_text(
                                            "✅"
                                            "\n"
                                            "اشتراک یک ماهه تریدرزهال برای شما فعال شد"
                                            "\n"
                                            "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                       , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                        )    
                            return backToHome 
                        else:
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "تراکنش شما از لحاظ زمانی درست نیست لطفا به پشتیبانی پیام دهید"
                                , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                    else:
                        print("meghdare varizi dorost nist")
                        update.message.reply_text(
                            "⛔️"
                            "\n"
                            "مقدار واریزیتان درست نیست لطفا به پشتیبانی پیام دهید"
                            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                            )
                        return backToHome
    else:
        update.message.reply_text(
            "⛔️"
            "\n"
            "آدرس کیف پولتان در تراکنش های ما پیدا نشد ، در صورت مشکل با پشتیبانی در ارتباط باشید "
            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
        )
        return backToHome
#-------------------------------------

def howtopayth2(update : Update, context: CallbackContext):
    print("howtopayTh2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['Txid' , 'کیف پول'] , ['لغو درخواست']]
    update.message.reply_text(
        "لطفا نحوه پرداختتان را از طریق دکمه های منوی پایین انتخاب کنید"
    , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return AssetTh2

def assetTh2(update : Update, context: CallbackContext):
    print("assetTh2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    user = update.message.from_user['username']
    with open("./history.json" , "r") as historyFile:
        data = json.load(historyFile)
        # print(data)
        if len(data) > 0 :
            print("find")
            dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : ''
                }
            j = 0 
            for user in data:
                if user["username"] == update.message.from_user["username"]:
                    print("recieved")
                    update.message.reply_text(
                        "لطفا کد فرستاده شده در google authenticator  را برایمان ارسال کنید"
                    )
                    return CheckQrCodeTh2
                j = j + 1
                    
            else:
                print("cant recieved")
                with open ("./number.txt" , "r") as readingTextFile : 
                    data = readingTextFile.readlines()
                    print(data[0])
                    print(type(data[0]))
                    textdata = data[0]
                    aftertextdata = int(data[0]) + 1
                    t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                    print(t.now())
                    auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                    x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    print(auth_str)  
                    s = str(auth_str)
                    url = pyqrcode.create(s)
                    url.png(f'./{user}.png', scale = 6)
                    dict = {
                        "username" : update.message.from_user['username'],
                        "packages" : [],
                        "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    }
                    with open("./history.json" , "r") as readinghistoryFile:
                        data = json.load(readinghistoryFile)
                        with open("./history.json" , "w") as writingHistoryFile:
                            data.append(dict)
                            json.dump(data , writingHistoryFile , indent = 6)
                    # with open("./number.txt" , "w") as writingTextFile : 
                    #     writingTextFile.write(str(aftertextdata))
                    update.message.reply_text(
                            "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                  "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    ) 
                    context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
                    return CheckQrCodeTh2
        else:
            print("cant find")
            print("cant recieved")
            with open ("./number.txt" , "r") as readingTextFile : 
                data = readingTextFile.readlines()
                print(data[0])
                print(type(data[0]))
                textdata = data[0]
                aftertextdata = int(data[0]) + 1
                t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                print(t.now())
                auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                print(auth_str)  
                s = str(auth_str)
                url = pyqrcode.create(s)
                url.png(f'./{user}.png', scale = 6)
                dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                }
                with open("./history.json" , "r") as readinghistoryFile:
                    data = json.load(readinghistoryFile)
                    with open("./history.json" , "w") as writingHistoryFile:
                        data.append(dict)
                        json.dump(data , writingHistoryFile , indent = 6)
                # with open("./number.txt" , "w") as writingTextFile : 
                #     writingTextFile.write(str(aftertextdata))
                update.message.reply_text(
                        "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                        "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    )
                context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
            return CheckQrCodeTh2

def checkingQRcodeTh2(update : Update, context: CallbackContext):
    print("checkingQRcodeTh2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    with open("./history.json" , "r") as historyFile : 
        data = json.load(historyFile)
        for user in data:
            if user["username"] == update.message.from_user["username"]:
                t = pyotp.TOTP(user['secret'])
                print(update.message.text)
                print("=======")
                print(t.now())
                print("======")
                print(type(update.message.text))
                print("=======")
                print(type(t.now()))
                if str(update.message.text) == str(t.now()):
                    update.message.reply_text(
                        "رمز دوم شما با موفقیت تایید شد"
                        "\n"
                        "لطفا آدرس کیف پول خود را ارسال کنید"
                    )
                    return CheckAssetTh2
                else:
                    update.message.reply_text(
                        "رمز دوم شما درست نیست لطفا دوباره وارد کنید"
                    )
            break
        else:
            print("tamaaaam")

def checkingassetTh2(update : Update, context: CallbackContext):
    print("checkingasseth2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا منتظر بمانید در حال بررسی درخواستتان..."
    )
    print(update.message.text)
    reply_keyboard = [['برگشت به محصولات']]
    url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
    websitetronData = requests.post(url)
    tronJsonData = websitetronData.json()
    tronJsonDataData = tronJsonData["data"]
    # print(tronJsonDataData)
    for asset in tronJsonDataData:
        if asset['transferFromAddress'] == update.message.text:
            print(asset)
            if asset["confirmed"] == True:
                with open ("./teronscan.json" , "r") as readingHistoryData : 
                    data = json.load(readingHistoryData)
                update.message.reply_text("آدرس کیف پولتان در تراکنش ها پیدا شد در حال بررسی مقدار واریزی...")
                for history in data:
                    if history["from_address"] == asset['transferFromAddress']:
                        print("addres ha barabar")
                        if history['transaction_id'] == asset['transactionHash']:
                            print("addrese barabar txidsh sabt shode => ban")
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "این تراکنش قبلا ثبت شده است لطفا با پشتیبانی تماس بگیرید"
                                , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                else:
                    print("barresi amount")
                    if int(asset['amount']) < 102000000 and int(asset['amount']) > 98000000 : 
                        print("amount dorost bood")
                        update.message.reply_text("مقدار واریزی درست است در حال بررسی زمان پرداخت ...")
                        time.sleep(2)
                        dateTime = str(datetime.datetime.now())
                        timeing = dateTime.split(" ")
                        hour = timeing[1].split(":")
                        print(hour[0])
                        timestampTime = asset["timestamp"]
                        tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                        timingteron = str(datetime.datetime.utcfromtimestamp(timestampTime / 1e3))
                        timingteron2 = timingteron.split(" ")
                        timingteron3 = timingteron2[1].split(":")
                        print(timingteron3[0])
                        if int(timingteron3[0]) >= int(hour[0]) - 1 and int(timingteron3[0]) <= int(hour[0]) :
                            update.message.reply_text(
                                "تراکنش شما از لحاظ زمانی نیز درست می باشد لطفا صبر کنید تا اشتراک تان فعال شود..."
                            ) 
                            tehranTime = str(tehranTime)
                            newDict = {
                                "amount" : asset["amount"],
                                "from_address" : asset["transferFromAddress"],
                                "to_address" : asset["transferToAddress"],
                                "confirmed" : asset["confirmed"],
                                "transaction_id" : asset["transactionHash"],
                                "timestamp" : tehranTime
                            }
                            with open("./teronscan.json" , "r") as teronscanreadingfile:
                                logData = json.load(teronscanreadingfile)
                            logData.append(newDict)
                            with open("./teronscan.json" , "w") as teronscanwritingfile:
                                json.dump(logData , teronscanwritingfile , indent = 6)
                            username = update.message.from_user['username']
                            with open("./myfile.json" , "r") as readJsonFile:
                                jsonFileDicts = json.load(readJsonFile)
                                historyDict = {
                                            "username" :  update.message.from_user['username'],
                                            "packages" : [],
                                            "secret" : ""
                                        }
                                print('1')
                                with open("history.json" , "r") as readinghitoryFile :
                                    historyData = json.load(readinghitoryFile)
                                    if len(historyData) > 0:
                                        print(historyData)
                                        j = 0
                                        for userHistoryData in historyData:
                                            print(userHistoryData)
                                            print('2')
                                            if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                print('3')
                                                historyDict["secret"] = userHistoryData["secret"]
                                                for i in userHistoryData["packages"]:
                                                    historyDict["packages"].append(i)
                                                historyData.remove(historyData[j])
                                                historyDict['packages'].append("اشتراک سه ماهه تریدرزهال")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as historyJsonFile :
                                                    json.dump(historyData , historyJsonFile , indent = 6)
                                                    break 
                                            j = j + 1    
                                        else:
                                            print('4')
                                            historyDict['packages'].append("اشتراک سه ماهه تریدرزهال")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                                    
                                    else:
                                        print('5')
                                        historyDict['packages'].append("اشتراک سه ماهه تریدرزهال")
                                        historyData.append(historyDict)
                                        with open("history.json" , "w") as writingHistoryFile :
                                            json.dump(historyData , writingHistoryFile , indent = 6)
                                for jsonFiledic in jsonFileDicts:
                                    if jsonFiledic["telegram_id"] == username:
                        
                                        # print(jsonFiledic["user_id"])
                                        uid = jsonFiledic["user_id"]
                                        url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=15"
                                        requests.get(url1)
                                        time.sleep(1)
                                        url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=15"
                                        # 1 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 2 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 3 time
                                        requests.get(url2)
                                        update.message.reply_text(
                                            "✅"
                                            "\n"
                                            "اشتراک سه ماهه تریدرزهال برای شما فعل شد"
                                            "\n"
                                            "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                       , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                        )    
                            return backToHome 
                        else:
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "تراکنش شما از لحاظ زمانی درست نیست لطفا به پشتیبانی پیام دهید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                    else:
                        print("meghdare varizi dorost nist")
                        update.message.reply_text(
                            "⛔️"
                                "\n"
                            "مقدار واریزیتان درست نیست لطفا به پشتیبانی پیام دهید"
                            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                            )
                        return backToHome
    else:
        update.message.reply_text(
            "⛔️"
            "\n"
            "آدرس کیف پولتان در تراکنش های ما پیدا نشد ، در صورت مشکل با پشتیبانی در ارتباط باشید "
            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
        )
        return backToHome
#-------------------------------------

def howtopayth3(update : Update, context: CallbackContext):
    print("howtopayTh3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['Txid' , 'کیف پول'] , ['لغو درخواست']]
    update.message.reply_text(
        "لطفا نحوه پرداختتان را از طریق دکمه های منوی پایین انتخاب کنید"
    , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return AssetTh3

def assetTh3(update : Update, context: CallbackContext):
    print("assetTh3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    user = update.message.from_user['username']
    with open("./history.json" , "r") as historyFile:
        data = json.load(historyFile)
        # print(data)
        if len(data) > 0 :
            print("find")
            dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : ''
                }
            j = 0 
            for user in data:
                if user["username"] == update.message.from_user["username"]:
                    print("recieved")
                    update.message.reply_text(
                        "لطفا کد فرستاده شده در google authenticator  را برایمان ارسال کنید"
                    )
                    return CheckQrCodeTh3
                j = j + 1
                    
            else:
                print("cant recieved")
                with open ("./number.txt" , "r") as readingTextFile : 
                    data = readingTextFile.readlines()
                    print(data[0])
                    print(type(data[0]))
                    textdata = data[0]
                    aftertextdata = int(data[0]) + 1
                    t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                    print(t.now())
                    auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                    x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    print(auth_str)  
                    s = str(auth_str)
                    url = pyqrcode.create(s)
                    url.png(f'./{user}.png', scale = 6)
                    dict = {
                        "username" : update.message.from_user['username'],
                        "packages" : [],
                        "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    }
                    with open("./history.json" , "r") as readinghistoryFile:
                        data = json.load(readinghistoryFile)
                        with open("./history.json" , "w") as writingHistoryFile:
                            data.append(dict)
                            json.dump(data , writingHistoryFile , indent = 6)
                    # with open("./number.txt" , "w") as writingTextFile : 
                    #     writingTextFile.write(str(aftertextdata))
                    update.message.reply_text(
                            "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                    "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    ) 
                    context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
                    return CheckQrCodeTh3
        else:
            print("cant find")
            print("cant recieved")
            with open ("./number.txt" , "r") as readingTextFile : 
                data = readingTextFile.readlines()
                print(data[0])
                print(type(data[0]))
                textdata = data[0]
                aftertextdata = int(data[0]) + 1
                t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                print(t.now())
                auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                print(auth_str)  
                s = str(auth_str)
                url = pyqrcode.create(s)
                url.png(f'./{user}.png', scale = 6)
                x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                }
                with open("./history.json" , "r") as readinghistoryFile:
                    data = json.load(readinghistoryFile)
                    with open("./history.json" , "w") as writingHistoryFile:
                        data.append(dict)
                        json.dump(data , writingHistoryFile , indent = 6)
                # with open("./number.txt" , "w") as writingTextFile : 
                #     writingTextFile.write(str(aftertextdata))
                update.message.reply_text(
                        "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                  "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    )
                context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
                print(update.message)
            return CheckQrCodeTh3

def checkingQRcodeTh3(update : Update, context: CallbackContext):
    print("checkingQRcodeTh3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    with open("./history.json" , "r") as historyFile : 
        data = json.load(historyFile)
        for user in data:
            if user["username"] == update.message.from_user["username"]:
                t = pyotp.TOTP(user['secret'])
                print(update.message.text)
                print(t.now())
                print(type(update.message.text))
                print(type(t.now()))
                if str(update.message.text) == str(t.now()):
                    update.message.reply_text(
                        "رمز دوم شما با موفقیت تایید شد"
                        "\n"
                        "لطفا آدرس کیف پول خود را ارسال کنید"
                    )
                    return CheckAssetTh3
                else:
                    update.message.reply_text(
                        "رمز دوم شما درست نیست لطفا دوباره وارد کنید"
                    )
            break
        else:
            print("tamaaaam")

def checkingassetTh3(update : Update, context: CallbackContext):
    print("checkingasseth3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا منتظر بمانید در حال بررسی درخواستتان..."
    )
    print(update.message.text)
    reply_keyboard = [['برگشت به محصولات']]
    url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
    websitetronData = requests.post(url)
    tronJsonData = websitetronData.json()
    tronJsonDataData = tronJsonData["data"]
    # print(tronJsonDataData)
    for asset in tronJsonDataData:
        if asset['transferFromAddress'] == update.message.text:
            print(asset)
            if asset["confirmed"] == True:
                with open ("./teronscan.json" , "r") as readingHistoryData : 
                    data = json.load(readingHistoryData)
                update.message.reply_text("آدرس کیف پولتان در تراکنش ها پیدا شد در حال بررسی مقدار واریزی...")
                for history in data:
                    if history["from_address"] == asset['transferFromAddress']:
                        print("addres ha barabar")
                        if history['transaction_id'] == asset['transactionHash']:
                            print("addrese barabar txidsh sabt shode => ban")
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "این تراکنش قبلا ثبت شده است لطفا با پشتیبانی تماس بگیرید"
                                , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                else:
                    print("barresi amount")
                    if int(asset['amount']) < 202000000 and int(asset['amount']) > 198000000 : 
                        print("amount dorost bood")
                        update.message.reply_text("مقدار واریزی درست است در حال بررسی زمان پرداخت ...")
                        time.sleep(2)
                        dateTime = str(datetime.datetime.now())
                        timeing = dateTime.split(" ")
                        hour = timeing[1].split(":")
                        print(hour[0])
                        timestampTime = asset["timestamp"]
                        tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                        timingteron = str(datetime.datetime.utcfromtimestamp(timestampTime / 1e3))
                        timingteron2 = timingteron.split(" ")
                        timingteron3 = timingteron2[1].split(":")
                        print(timingteron3[0])
                        if int(timingteron3[0]) >= int(hour[0]) - 1 and int(timingteron3[0]) <= int(hour[0]) :
                            update.message.reply_text(
                                "تراکنش شما از لحاظ زمانی نیز درست می باشد لطفا صبر کنید تا اشتراک تان فعال شود..."
                            ) 
                            tehranTime = str(tehranTime)
                            newDict = {
                                "amount" : asset["amount"],
                                "from_address" : asset["transferFromAddress"],
                                "to_address" : asset["transferToAddress"],
                                "confirmed" : asset["confirmed"],
                                "transaction_id" : asset["transactionHash"],
                                "timestamp" : tehranTime
                            }
                            with open("./teronscan.json" , "r") as teronscanreadingfile:
                                logData = json.load(teronscanreadingfile)
                            logData.append(newDict)
                            with open("./teronscan.json" , "w") as teronscanwritingfile:
                                json.dump(logData , teronscanwritingfile , indent = 6)
                            username = update.message.from_user['username']
                            with open("./myfile.json" , "r") as readJsonFile:
                                jsonFileDicts = json.load(readJsonFile)
                                historyDict = {
                                            "username" :  update.message.from_user['username'],
                                            "packages" : [],
                                            "secret" : ""
                                        }
                                print('1')
                                with open("history.json" , "r") as readinghitoryFile :
                                    historyData = json.load(readinghitoryFile)
                                    if len(historyData) > 0:
                                        print(historyData)
                                        j = 0
                                        for userHistoryData in historyData:
                                            print(userHistoryData)
                                            print('2')
                                            if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                print('3')
                                                historyDict["secret"] = userHistoryData["secret"]
                                                for i in userHistoryData["packages"]:
                                                    historyDict["packages"].append(i)
                                                historyData.remove(historyData[j])
                                                historyDict['packages'].append("اشتراک یک ساله تریدرزهال")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as historyJsonFile :
                                                    json.dump(historyData , historyJsonFile , indent = 6)
                                                    break 
                                            j = j + 1    
                                        else:
                                            print('4')
                                            historyDict['packages'].append("اشتراک یک ساله تریدرزهال")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                                    
                                    else:
                                        print('5')
                                        historyDict['packages'].append("اشتراک یک ساله تریدرزهال")
                                        historyData.append(historyDict)
                                        with open("history.json" , "w") as writingHistoryFile :
                                            json.dump(historyData , writingHistoryFile , indent = 6)
                                for jsonFiledic in jsonFileDicts:
                                    if jsonFiledic["telegram_id"] == username:
                        
                                        # print(jsonFiledic["user_id"])
                                        uid = jsonFiledic["user_id"]
                                        url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=15"
                                        requests.get(url1)
                                        time.sleep(1)
                                        url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=15"
                                        # 1 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 2 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 3 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 4 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 5 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 6 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 7 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 8 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 9 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 10 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 11 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 12 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        update.message.reply_text(
                                            "✅"
                                            "\n"
                                            "اشتراک یک ساله تریدرزهال برای شما فعال شد"
                                            "\n"
                                            "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                       , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                        )    
                            return backToHome 
                        else:
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "تراکنش شما از لحاظ زمانی درست نیست لطفا به پشتیبانی پیام دهید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                    else:
                        print("meghdare varizi dorost nist")
                        update.message.reply_text(
                            "⛔️"
                                "\n"
                            "مقدار واریزیتان درست نیست لطفا به پشتیبانی پیام دهید"
                            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                            )
                        return backToHome
    else:
        update.message.reply_text(
            "⛔️"
             "\n"
            "آدرس کیف پولتان در تراکنش های ما پیدا نشد ، در صورت مشکل با پشتیبانی در ارتباط باشید "
            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
        )
        return backToHome

#-------------------------------------
def howtopayvip1(update : Update, context: CallbackContext):
    print("howtopayvip1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['Txid' , 'کیف پول'] , ['لغو درخواست']]
    update.message.reply_text(
        "لطفا نحوه پرداختتان را از طریق دکمه های منوی پایین انتخاب کنید"
    , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return AssetVip1

def howtopayvip2(update : Update, context: CallbackContext):
    print("howtopayvip2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['Txid' , 'کیف پول'] , ['لغو درخواست']]
    update.message.reply_text(
        "لطفا نحوه پرداختتان را از طریق دکمه های منوی پایین انتخاب کنید"
    , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return AssetVip2

def howtopayvip3(update : Update, context: CallbackContext):
    print("howtopayvip3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['Txid' , 'کیف پول'] , ['لغو درخواست']]
    update.message.reply_text(
        "لطفا نحوه پرداختتان را از طریق دکمه های منوی پایین انتخاب کنید"
    , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return AssetVip3

def assetvip1(update : Update, context: CallbackContext):
    print("assetvip1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    user = update.message.from_user['username']
    with open("./history.json" , "r") as historyFile:
        data = json.load(historyFile)
        # print(data)
        if len(data) > 0 :
            print("find")
            dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : ''
                }
            j = 0 
            for user in data:
                if user["username"] == update.message.from_user["username"]:
                    print("recieved")
                    update.message.reply_text(
                        "لطفا کد فرستاده شده در google authenticator  را برایمان ارسال کنید"
                    )
                    return CheckQrCodeVip1
                j = j + 1
                    
            else:
                print("cant recieved")
                with open ("./number.txt" , "r") as readingTextFile : 
                    data = readingTextFile.readlines()
                    print(data[0])
                    print(type(data[0]))
                    textdata = data[0]
                    aftertextdata = int(data[0]) + 1
                    t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                    print(t.now())
                    auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                    print(auth_str)  
                    s = str(auth_str)
                    url = pyqrcode.create(s)
                    url.png(f'./{user}.png', scale = 6)
                    x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    dict = {
                        "username" : update.message.from_user['username'],
                        "packages" : [],
                        "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    }
                    with open("./history.json" , "r") as readinghistoryFile:
                        data = json.load(readinghistoryFile)
                        with open("./history.json" , "w") as writingHistoryFile:
                            data.append(dict)
                            json.dump(data , writingHistoryFile , indent = 6)
                    # with open("./number.txt" , "w") as writingTextFile : 
                    #     writingTextFile.write(str(aftertextdata))
                    update.message.reply_text(
                            "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                   "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    ) 
                    context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
                    return CheckQrCodeVip1
        else:
            print("cant find")
            print("cant recieved")
            with open ("./number.txt" , "r") as readingTextFile : 
                data = readingTextFile.readlines()
                print(data[0])
                print(type(data[0]))
                textdata = data[0]
                aftertextdata = int(data[0]) + 1
                t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                print(t.now())
                auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                print(auth_str)  
                s = str(auth_str)
                url = pyqrcode.create(s)
                url.png(f'./{user}.png', scale = 6)
                dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                }
                with open("./history.json" , "r") as readinghistoryFile:
                    data = json.load(readinghistoryFile)
                    with open("./history.json" , "w") as writingHistoryFile:
                        data.append(dict)
                        json.dump(data , writingHistoryFile , indent = 6)
                # with open("./number.txt" , "w") as writingTextFile : 
                #     writingTextFile.write(str(aftertextdata))
                update.message.reply_text(
                        "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                   "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    )
                context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
            return CheckQrCodeVip1

#--------------------------------------------------------------------

def assetvip2(update : Update, context: CallbackContext):
    print("assetvip2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    user = update.message.from_user['username']
    with open("./history.json" , "r") as historyFile:
        data = json.load(historyFile)
        # print(data)
        if len(data) > 0 :
            print("find")
            dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : ''
                }
            j = 0 
            for user in data:
                if user["username"] == update.message.from_user["username"]:
                    print("recieved")
                    update.message.reply_text(
                        "لطفا کد فرستاده شده در google authenticator  را برایمان ارسال کنید"
                    )
                    return CheckQrCodeVip2
                j = j + 1
                    
            else:
                print("cant recieved")
                with open ("./number.txt" , "r") as readingTextFile : 
                    data = readingTextFile.readlines()
                    print(data[0])
                    print(type(data[0]))
                    textdata = data[0]
                    aftertextdata = int(data[0]) + 1
                    t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                    print(t.now())
                    auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                    print(auth_str)  
                    s = str(auth_str)
                    url = pyqrcode.create(s)
                    url.png(f'./{user}.png', scale = 6)
                    x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    dict = {
                        "username" : update.message.from_user['username'],
                        "packages" : [],
                        "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    }
                    with open("./history.json" , "r") as readinghistoryFile:
                        data = json.load(readinghistoryFile)
                        with open("./history.json" , "w") as writingHistoryFile:
                            data.append(dict)
                            json.dump(data , writingHistoryFile , indent = 6)
                    # with open("./number.txt" , "w") as writingTextFile : 
                    #     writingTextFile.write(str(aftertextdata))
                    update.message.reply_text(
                            "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                  "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    ) 
                    context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
                    return CheckQrCodeVip2
        else:
            print("cant find")
            print("cant recieved")
            with open ("./number.txt" , "r") as readingTextFile : 
                data = readingTextFile.readlines()
                print(data[0])
                print(type(data[0]))
                textdata = data[0]
                aftertextdata = int(data[0]) + 1
                t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                print(t.now())
                auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                print(auth_str)  
                s = str(auth_str)
                url = pyqrcode.create(s)
                url.png(f'./{user}.png', scale = 6)
                x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                }
                with open("./history.json" , "r") as readinghistoryFile:
                    data = json.load(readinghistoryFile)
                    with open("./history.json" , "w") as writingHistoryFile:
                        data.append(dict)
                        json.dump(data , writingHistoryFile , indent = 6)
                # with open("./number.txt" , "w") as writingTextFile : 
                #     writingTextFile.write(str(aftertextdata))
                update.message.reply_text(
                        "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                   "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    )
                context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
            return CheckQrCodeVip2

#--------------------------------------------------------------------

def assetvip3(update : Update, context: CallbackContext):
    print("assetvip3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    user = update.message.from_user['username']
    with open("./history.json" , "r") as historyFile:
        data = json.load(historyFile)
        # print(data)
        if len(data) > 0 :
            print("find")
            dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : ''
                }
            j = 0 
            for user in data:
                if user["username"] == update.message.from_user["username"]:
                    print("recieved")
                    update.message.reply_text(
                        "لطفا کد فرستاده شده در google authenticator  را برایمان ارسال کنید"
                    )
                    return CheckQrCodeVip3
                j = j + 1
                    
            else:
                print("cant recieved")
                with open ("./number.txt" , "r") as readingTextFile : 
                    data = readingTextFile.readlines()
                    print(data[0])
                    print(type(data[0]))
                    textdata = data[0]
                    aftertextdata = int(data[0]) + 1
                    t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                    print(t.now())
                    auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                    print(auth_str)  
                    s = str(auth_str)
                    url = pyqrcode.create(s)
                    url.png(f'./{user}.png', scale = 6)
                    x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    dict = {
                        "username" : update.message.from_user['username'],
                        "packages" : [],
                        "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                    }
                    with open("./history.json" , "r") as readinghistoryFile:
                        data = json.load(readinghistoryFile)
                        with open("./history.json" , "w") as writingHistoryFile:
                            data.append(dict)
                            json.dump(data , writingHistoryFile , indent = 6)
                    # with open("./number.txt" , "w") as writingTextFile : 
                    #     writingTextFile.write(str(aftertextdata))
                    update.message.reply_text(
                            "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                  "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    ) 
                    context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
                    return CheckQrCodeVip3
        else:
            print("cant find")
            print("cant recieved")
            with open ("./number.txt" , "r") as readingTextFile : 
                data = readingTextFile.readlines()
                print(data[0])
                print(type(data[0]))
                textdata = data[0]
                aftertextdata = int(data[0]) + 1
                t = pyotp.TOTP(str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8')))
                print(t.now())
                auth_str = t.provisioning_uri(name = str(user) , issuer_name = "Rastad")
                print(auth_str)  
                s = str(auth_str)
                url = pyqrcode.create(s)
                url.png(f'./{user}.png', scale = 6)
                x = str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                dict = {
                    "username" : update.message.from_user['username'],
                    "packages" : [],
                    "secret" : str(base64.b32encode(bytearray(f"{user}",'utf-8')).decode('utf-8'))
                }
                with open("./history.json" , "r") as readinghistoryFile:
                    data = json.load(readinghistoryFile)
                    with open("./history.json" , "w") as writingHistoryFile:
                        data.append(dict)
                        json.dump(data , writingHistoryFile , indent = 6)
                # with open("./number.txt" , "w") as writingTextFile : 
                #     writingTextFile.write(str(aftertextdata))
                update.message.reply_text(
                        "بارکد QR زیر بر اساس آیدی تلگرام شما ساخته شده است "
                        "\n"
                        "لطفا بارکد را در اپلیکیشن  google Authenticator  اسکن کرده و رمز یکبار مصرف را برایمان بفرستید"
                   "\n"
                        "یا میتوانید از رمز زیر استفاده کنید : "
                        "\n"
                        f"{x}"
                    )
                context.bot.send_document(chat_id=update.message.from_user['id'], document=open(f"./{user}.png", 'rb'), filename=f'./qrcode.png')
            return CheckQrCodeVip3

#--------------------------------------------------------------------
def checkingQRcodevip1(update : Update, context: CallbackContext):
    print("checkingQRcodevip1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    with open("./history.json" , "r") as historyFile : 
        data = json.load(historyFile)
        for user in data:
            if user["username"] == update.message.from_user["username"]:
                t = pyotp.TOTP(user['secret'])
                print(update.message.text)
                print(t.now())
                print(type(update.message.text))
                print(type(t.now()))
                if str(update.message.text) == str(t.now()):
                    update.message.reply_text(
                        "رمز دوم شما با موفقیت تایید شد"
                        "\n"
                        "لطفا آدرس کیف پول خود را ارسال کنید"
                    )
                    return CheckAssetVip1
                else:
                    update.message.reply_text(
                        "رمز دوم شما درست نیست لطفا دوباره وارد کنید"
                    )
            break
        else:
            print("tamaaaam")

#----------------------------------------------

def checkingQRcodevip2(update : Update, context: CallbackContext):
    print("checkingQRcodevip2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    with open("./history.json" , "r") as historyFile : 
        data = json.load(historyFile)
        for user in data:
            if user["username"] == update.message.from_user["username"]:
                t = pyotp.TOTP(user['secret'])
                print(update.message.text)
                print(t.now())
                print(type(update.message.text))
                print(type(t.now()))
                if str(update.message.text) == str(t.now()):
                    update.message.reply_text(
                        "رمز دوم شما با موفقیت تایید شد"
                        "\n"
                        "لطفا آدرس کیف پول خود را ارسال کنید"
                    )
                    return CheckAssetVip2
                else:
                    update.message.reply_text(
                        "رمز دوم شما درست نیست لطفا دوباره وارد کنید"
                    )
            break
        else:
            print("tamaaaam")

#----------------------------------------------

def checkingQRcodevip3(update : Update, context: CallbackContext):
    print("checkingQRcodevip3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    with open("./history.json" , "r") as historyFile : 
        data = json.load(historyFile)
        for user in data:
            if user["username"] == update.message.from_user["username"]:
                t = pyotp.TOTP(user['secret'])
                print(update.message.text)
                print(t.now())
                print(type(update.message.text))
                print(type(t.now()))
                if str(update.message.text) == str(t.now()):
                    update.message.reply_text(
                        "رمز دوم شما با موفقیت تایید شد"
                        "\n"
                        "لطفا آدرس کیف پول خود را ارسال کنید"
                    )
                    return CheckAssetVip3
                else:
                    update.message.reply_text(
                        "رمز دوم شما درست نیست لطفا دوباره وارد کنید"
                    )
            break
        else:
            print("tamaaaam")

#---------------------------------------------
def checkingassetvip1(update : Update, context: CallbackContext):
    print("checkingassetvip1")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا منتظر بمانید در حال بررسی درخواستتان..."
    )
    print(update.message.text)
    reply_keyboard = [['برگشت به محصولات']]
    url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
    websitetronData = requests.post(url)
    tronJsonData = websitetronData.json()
    tronJsonDataData = tronJsonData["data"]
    # print(tronJsonDataData)
    for asset in tronJsonDataData:
        if asset['transferFromAddress'] == update.message.text:
            print(asset)
            if asset["confirmed"] == True:
                with open ("./teronscan.json" , "r") as readingHistoryData : 
                    data = json.load(readingHistoryData)
                update.message.reply_text("آدرس کیف پولتان در تراکنش ها پیدا شد در حال بررسی مقدار واریزی...")
                for history in data:
                    if history["from_address"] == asset['transferFromAddress']:
                        print("addres ha barabar")
                        if history['transaction_id'] == asset['transactionHash']:
                            print("addrese barabar txidsh sabt shode => ban")
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "این تراکنش قبلا ثبت شده است لطفا با پشتیبانی تماس بگیرید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                else:
                    print("barresi amount")
                    if int(asset['amount']) < 27000000 and int(asset['amount']) > 23000000 : 
                        print("amount dorost bood")
                        update.message.reply_text("مقدار واریزی درست است در حال بررسی زمان پرداخت ...")
                        time.sleep(2)
                        dateTime = str(datetime.datetime.now())
                        timeing = dateTime.split(" ")
                        hour = timeing[1].split(":")
                        print(hour[0])
                        timestampTime = asset["timestamp"]
                        tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                        timingteron = str(datetime.datetime.utcfromtimestamp(timestampTime / 1e3))
                        timingteron2 = timingteron.split(" ")
                        timingteron3 = timingteron2[1].split(":")
                        print(timingteron3[0])
                        if int(timingteron3[0]) >= int(hour[0]) - 1 and int(timingteron3[0]) <= int(hour[0]) :
                            update.message.reply_text(
                                "تراکنش شما از لحاظ زمانی نیز درست می باشد لطفا صبر کنید تا اشتراک تان فعال شود..."
                            ) 
                            tehranTime = str(tehranTime)
                            newDict = {
                                "amount" : asset["amount"],
                                "from_address" : asset["transferFromAddress"],
                                "to_address" : asset["transferToAddress"],
                                "confirmed" : asset["confirmed"],
                                "transaction_id" : asset["transactionHash"],
                                "timestamp" : tehranTime
                            }
                            with open("./teronscan.json" , "r") as teronscanreadingfile:
                                logData = json.load(teronscanreadingfile)
                            logData.append(newDict)
                            with open("./teronscan.json" , "w") as teronscanwritingfile:
                                json.dump(logData , teronscanwritingfile , indent = 6)
                            username = update.message.from_user['username']
                            with open("./myfile.json" , "r") as readJsonFile:
                                jsonFileDicts = json.load(readJsonFile)
                                historyDict = {
                                            "username" :  update.message.from_user['username'],
                                            "packages" : [],
                                            "secret" : ""
                                        }
                                print('1')
                                with open("history.json" , "r") as readinghitoryFile :
                                    historyData = json.load(readinghitoryFile)
                                    if len(historyData) > 0:
                                        print(historyData)
                                        j = 0
                                        for userHistoryData in historyData:
                                            print(userHistoryData)
                                            print('2')
                                            if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                print('3')
                                                historyDict["secret"] = userHistoryData["secret"]
                                                for i in userHistoryData["packages"]:
                                                    historyDict["packages"].append(i)
                                                historyData.remove(historyData[j])
                                                historyDict['packages'].append("اشتراک یک ماهه vip")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as historyJsonFile :
                                                    json.dump(historyData , historyJsonFile , indent = 6)
                                                    break 
                                            j = j + 1    
                                        else:
                                            print('4')
                                            historyDict['packages'].append("اشتراک یک ماهه vip")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                                    
                                    else:
                                        print('5')
                                        historyDict['packages'].append("اشتراک یک ماهه vip")
                                        historyData.append(historyDict)
                                        with open("history.json" , "w") as writingHistoryFile :
                                            json.dump(historyData , writingHistoryFile , indent = 6)
                                for jsonFiledic in jsonFileDicts:
                                    if jsonFiledic["telegram_id"] == username:
                        
                                        # print(jsonFiledic["user_id"])
                                        uid = jsonFiledic["user_id"]
                                        url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=1"
                                        requests.get(url1)
                                        time.sleep(1)
                                        url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=1"
                                        # 1 time
                                        requests.get(url2)
                                        update.message.reply_text(
                                            "✅"
                                            "\n"
                                            "اشتراک یک ماهه vip  برای شما فعال شد"
                                            "\n"
                                            "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                        , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                        )    
                            return backToHome 
                        else:
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "تراکنش شما از لحاظ زمانی درست نیست لطفا به پشتیبانی پیام دهید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                    else:
                        print("meghdare varizi dorost nist")
                        update.message.reply_text(
                            "⛔️"
                                "\n"
                            "مقدار واریزیتان درست نیست لطفا به پشتیبانی پیام دهید"
                            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                            )
                        return backToHome
    else:
        update.message.reply_text(
            "⛔️"
             "\n"
            "آدرس کیف پولتان در تراکنش های ما پیدا نشد ، در صورت مشکل با پشتیبانی در ارتباط باشید "
            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
        )
        return backToHome


#------------------------------------

def checkingassetvip2(update : Update, context: CallbackContext):
    print("checkingassetvip2")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا منتظر بمانید در حال بررسی درخواستتان..."
    )
    reply_keyboard = [['برگشت به محصولات']]
    print(update.message.text)
    url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
    websitetronData = requests.post(url)
    tronJsonData = websitetronData.json()
    tronJsonDataData = tronJsonData["data"]
    # print(tronJsonDataData)
    for asset in tronJsonDataData:
        if asset['transferFromAddress'] == update.message.text:
            print(asset)
            if asset["confirmed"] == True:
                with open ("./teronscan.json" , "r") as readingHistoryData : 
                    data = json.load(readingHistoryData)
                    update.message.reply_text(
                    
                    "آدرس کیف پولتان در تراکنش ها پیدا شد در حال بررسی مقدار واریزی..."
                   
                    )
                # return backToHome
                for history in data:
                    if history["from_address"] == asset['transferFromAddress']:
                        print("addres ha barabar")
                        if history['transaction_id'] == asset['transactionHash']:
                            print("addrese barabar txidsh sabt shode => ban")
                            update.message.reply_text(
                                "⛔️"
                    "\n"
                                "این تراکنش قبلا ثبت شده است لطفا با پشتیبانی تماس بگیرید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                else:
                    print("barresi amount")
                    if int(asset['amount']) < 72000000 and int(asset['amount']) > 68000000 : 
                        print("amount dorost bood")
                        update.message.reply_text("مقدار واریزی درست است در حال بررسی زمان پرداخت ...")
                        time.sleep(2)
                        dateTime = str(datetime.datetime.now())
                        timeing = dateTime.split(" ")
                        hour = timeing[1].split(":")
                        print(hour[0])
                        timestampTime = asset["timestamp"]
                        tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                        timingteron = str(datetime.datetime.utcfromtimestamp(timestampTime / 1e3))
                        timingteron2 = timingteron.split(" ")
                        timingteron3 = timingteron2[1].split(":")
                        print(timingteron3[0])
                        if int(timingteron3[0]) >= int(hour[0]) - 1 and int(timingteron3[0]) <= int(hour[0]) :
                            update.message.reply_text(
                                "تراکنش شما از لحاظ زمانی نیز درست می باشد لطفا صبر کنید تا اشتراک تان فعال شود..."
                            ) 
                            tehranTime = str(tehranTime)
                            newDict = {
                                "amount" : asset["amount"],
                                "from_address" : asset["transferFromAddress"],
                                "to_address" : asset["transferToAddress"],
                                "confirmed" : asset["confirmed"],
                                "transaction_id" : asset["transactionHash"],
                                "timestamp" : tehranTime
                            }
                            with open("./teronscan.json" , "r") as teronscanreadingfile:
                                logData = json.load(teronscanreadingfile)
                            logData.append(newDict)
                            with open("./teronscan.json" , "w") as teronscanwritingfile:
                                json.dump(logData , teronscanwritingfile , indent = 6)
                            username = update.message.from_user['username']
                            with open("./myfile.json" , "r") as readJsonFile:
                                jsonFileDicts = json.load(readJsonFile)
                                historyDict = {
                                            "username" :  update.message.from_user['username'],
                                            "packages" : [],
                                            "secret" : ""
                                        }
                                print('1')
                                with open("history.json" , "r") as readinghitoryFile :
                                    historyData = json.load(readinghitoryFile)
                                    if len(historyData) > 0:
                                        print(historyData)
                                        j = 0
                                        for userHistoryData in historyData:
                                            print(userHistoryData)
                                            print('2')
                                            if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                print('3')
                                                historyDict["secret"] = userHistoryData["secret"]
                                                for i in userHistoryData["packages"]:
                                                    historyDict["packages"].append(i)
                                                historyData.remove(historyData[j])
                                                historyDict['packages'].append("اشتراک سه ماهه vip")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as historyJsonFile :
                                                    json.dump(historyData , historyJsonFile , indent = 6)
                                                    break 
                                            j = j + 1    
                                        else:
                                            print('4')
                                            historyDict['packages'].append("اشتراک سه ماهه vip")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                                    
                                    else:
                                        print('5')
                                        historyDict['packages'].append("اشتراک سه ماهه vip")
                                        historyData.append(historyDict)
                                        with open("history.json" , "w") as writingHistoryFile :
                                            json.dump(historyData , writingHistoryFile , indent = 6)
                                for jsonFiledic in jsonFileDicts:
                                    if jsonFiledic["telegram_id"] == username:
                        
                                        # print(jsonFiledic["user_id"])
                                        uid = jsonFiledic["user_id"]
                                        url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=1"
                                        requests.get(url1)
                                        time.sleep(1)
                                        url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=1"
                                        # 1 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 2 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 3 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        update.message.reply_text(
                                            "✅"
                                            "\n"
                                            "اشتراک سه ماهه vip  راستاد برای شما فعال شد"
                                            "\n"
                                            "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                        )    
                            return backToHome 
                        else:
                            update.message.reply_text(
                                "⛔️"
                    "\n"
                                "تراکنش شما از لحاظ زمانی درست نیست لطفا به پشتیبانی پیام دهید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                    else:
                        print("meghdare varizi dorost nist")
                        update.message.reply_text(
                            "⛔️"
                    "\n"
                            "مقدار واریزیتان درست نیست لطفا به پشتیبانی پیام دهید"
                            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                            )
                        return backToHome
    else:
        update.message.reply_text(
            "⛔️"
                    "\n"
            "آدرس کیف پولتان در تراکنش های ما پیدا نشد ، در صورت مشکل با پشتیبانی در ارتباط باشید "
            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
        )
        return backToHome
#----------------------------------------

def checkingassetvip3(update : Update, context: CallbackContext):
    print("checkingassetvip3")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا منتظر بمانید در حال بررسی درخواستتان..."
    )
    reply_keyboard = [['برگشت به محصولات']]
    print(update.message.text)
    url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
    websitetronData = requests.post(url)
    tronJsonData = websitetronData.json()
    tronJsonDataData = tronJsonData["data"]
    # print(tronJsonDataData)
    for asset in tronJsonDataData:
        if asset['transferFromAddress'] == update.message.text:
            print(asset)
            if asset["confirmed"] == True:
                with open ("./teronscan.json" , "r") as readingHistoryData : 
                    data = json.load(readingHistoryData)
                update.message.reply_text("آدرس کیف پولتان در تراکنش ها پیدا شد در حال بررسی مقدار واریزی...")
                for history in data:
                    if history["from_address"] == asset['transferFromAddress']:
                        print("addres ha barabar")
                        if history['transaction_id'] == asset['transactionHash']:
                            print("addrese barabar txidsh sabt shode => ban")
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "این تراکنش قبلا ثبت شده است لطفا با پشتیبانی تماس بگیرید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                else:
                    print("barresi amount")
                    if int(asset['amount']) < 152000000 and int(asset['amount']) > 148000000 : 
                        print("amount dorost bood")
                        update.message.reply_text("مقدار واریزی درست است در حال بررسی زمان پرداخت ...")
                        time.sleep(2)
                        dateTime = str(datetime.datetime.now())
                        timeing = dateTime.split(" ")
                        hour = timeing[1].split(":")
                        print(hour[0])
                        timestampTime = asset["timestamp"]
                        tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                        timingteron = str(datetime.datetime.utcfromtimestamp(timestampTime / 1e3))
                        timingteron2 = timingteron.split(" ")
                        timingteron3 = timingteron2[1].split(":")
                        print(timingteron3[0])
                        if int(timingteron3[0]) >= int(hour[0]) - 1 and int(timingteron3[0]) <= int(hour[0]) :
                            update.message.reply_text(
                                "تراکنش شما از لحاظ زمانی نیز درست می باشد لطفا صبر کنید تا اشتراک تان فعال شود..."
                            ) 
                            tehranTime = str(tehranTime)
                            newDict = {
                                "amount" : asset["amount"],
                                "from_address" : asset["transferFromAddress"],
                                "to_address" : asset["transferToAddress"],
                                "confirmed" : asset["confirmed"],
                                "transaction_id" : asset["transactionHash"],
                                "timestamp" : tehranTime
                            }
                            with open("./teronscan.json" , "r") as teronscanreadingfile:
                                logData = json.load(teronscanreadingfile)
                            logData.append(newDict)
                            with open("./teronscan.json" , "w") as teronscanwritingfile:
                                json.dump(logData , teronscanwritingfile , indent = 6)
                            username = update.message.from_user['username']
                            with open("./myfile.json" , "r") as readJsonFile:
                                jsonFileDicts = json.load(readJsonFile)
                                historyDict = {
                                            "username" :  update.message.from_user['username'],
                                            "packages" : [],
                                            "secret" : ""
                                        }
                                print('1')
                                with open("history.json" , "r") as readinghitoryFile :
                                    historyData = json.load(readinghitoryFile)
                                    if len(historyData) > 0:
                                        print(historyData)
                                        j = 0
                                        for userHistoryData in historyData:
                                            print(userHistoryData)
                                            print('2')
                                            if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                print('3')
                                                historyDict["secret"] = userHistoryData["secret"]
                                                for i in userHistoryData["packages"]:
                                                    historyDict["packages"].append(i)
                                                historyData.remove(historyData[j])
                                                historyDict['packages'].append("اشتراک یک ساله vip")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as historyJsonFile :
                                                    json.dump(historyData , historyJsonFile , indent = 6)
                                                    break 
                                            j = j + 1    
                                        else:
                                            print('4')
                                            historyDict['packages'].append("اشتراک یک ساله vip")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                                    
                                    else:
                                        print('5')
                                        historyDict['packages'].append("اشتراک یک ساله vip")
                                        historyData.append(historyDict)
                                        with open("history.json" , "w") as writingHistoryFile :
                                            json.dump(historyData , writingHistoryFile , indent = 6)
                                for jsonFiledic in jsonFileDicts:
                                    if jsonFiledic["telegram_id"] == username:
                        
                                        # print(jsonFiledic["user_id"])
                                        uid = jsonFiledic["user_id"]
                                        url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=1"
                                        requests.get(url1)
                                        time.sleep(1)
                                        url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=1"
                                        # 1 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 2 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 3 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 4 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 5 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 6 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 7 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 8 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 9 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 10 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 11 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        # 12 time
                                        requests.get(url2)
                                        time.sleep(1)
                                        update.message.reply_text(
                                            "✅"
                                            "\n"
                                            "اشتراک یک ساله vip  راستاد برای شما فعال شد"
                                            "\n"
                                            "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                       , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                        )    
                            return backToHome 
                        else:
                            update.message.reply_text(
                                "⛔️"
                                "\n"
                                "تراکنش شما از لحاظ زمانی درست نیست لطفا به پشتیبانی پیام دهید"
                                "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                                )
                            return backToHome
                    else:
                        print("meghdare varizi dorost nist")
                        update.message.reply_text(
                            "⛔️"
                                "\n"
                            "مقدار واریزیتان درست نیست لطفا به پشتیبانی پیام دهید"
                            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
                            )
                        return backToHome
    else:
        update.message.reply_text(
            "⛔️"
                                "\n"
            "آدرس کیف پولتان در تراکنش های ما پیدا نشد ، در صورت مشکل با پشتیبانی در ارتباط باشید "
            "\n"
            "@rastad_support"
            , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
        )
        return backToHome

#----------------------------------------
def viponemonth(update : Update, context: CallbackContext):
    '''in section vip we have three button one month running in this section'''
    print("vip one month run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا مقدار USDT روی شبکه 'Tron'TRC20 را به آدرس زیر بفرستید :"
        "\n\n"
        "TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf"
        "\n\n"
        "پس از واریز TxId خود را ارسال کنید"
    ) 
    return checkvipone

def viptwomonth(update : Update, context: CallbackContext):
    '''in section vip we have three button two month running in this section'''
    print("vip two month run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا مقدار USDT روی شبکه 'Tron'TRC20 را به آدرس زیر بفرستید :"
        "\n\n"
        "TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf"
        "\n\n"
        "پس از واریز TxId خود را ارسال کنید"
    ) 
    return checkviptwo

def vipthreemonth(update : Update, context: CallbackContext):
    '''in section vip we have three button three month running in this section'''
    print("vip three month run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا مقدار USDT روی شبکه 'Tron'TRC20 را به آدرس زیر بفرستید :"
        "\n\n"
        "TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf"
        "\n\n"
        "پس از واریز TxId خود را ارسال کنید"
    ) 
    return checkvipthree

def traderhall(update : Update, context: CallbackContext):
    '''section traderhall was running in this section'''
    print("trader hall run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['یک ساله 200 دلار','سه ماهه 100 دلار','یک ماهه 40 دلار'] , ['برگشت به انتخاب اشتراک ها']]
    update.message.reply_text(
        "مدت زمان اشتراک را انتخاب کنید : "
        , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return aftertraderzhal

def traderzhalonemonth(update : Update, context: CallbackContext):
    '''in section traderhall we have three button one month running in this section'''
    print("traderzhal one month run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا مقدار USDT روی شبکه 'Tron'TRC20 را به آدرس زیر بفرستید :"
        "\n\n"
        "TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf"
        "\n\n"
        "پس از واریز TxId خود را ارسال کنید"
    ) 
    return checktxidtraderhallone

def traderzhaltwomonth(update : Update, context: CallbackContext):
    '''in section traderhall we have three button two month running in this section'''
    print("traderzhal one month run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا مقدار USDT روی شبکه 'Tron'TRC20 را به آدرس زیر بفرستید :"
        "\n\n"
        "TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf"
        "\n\n"
        "پس از واریز TxId خود را ارسال کنید"
    ) 
    return checktxidtraderhalltwo

def traderzhalthreemonth(update : Update, context: CallbackContext):
    '''in section traderhall we have three button three month running in this section'''
    print("traderzhal three month run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    update.message.reply_text(
        "لطفا مقدار USDT روی شبکه 'Tron'TRC20 را به آدرس زیر بفرستید :"
        "\n\n"
        "TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf"
        "\n\n"
        "پس از واریز TxId خود را ارسال کنید"
    ) 
    return checktxidtraderhallthree

def checkingtxidtraderzhalthree(update : Update, context: CallbackContext):
    '''in this section checking txid and payment amount for traderhall three month section '''
    print("checkingtxid for traderzhallthree month is run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['برگشت به محصولات']]
    update.message.reply_text(
        "در حال بررسی TxId  لطفا منتظر بمانید..."
        , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    time.sleep(5)
    with open("./teronscan.json" , "r") as txIdsFile:
        txIds = json.load(txIdsFile)
        keyboard = [
        [
          InlineKeyboardButton("بات راستاد", callback_data="1" , url='tg://user?id=382215836'),
        ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        for txId in txIds:
            if txId["transaction_id"] == update.message.text:
                update.message.reply_text(
                    "⛔️"
                    "\n"
                   "این Txid قبلا استفاده شده است، اگر نیاز به کمک دارید لطفا به پشتیبانی راستاد پیام دهید:"
                "\n"
                "@Rastad_Support"
                ,reply_markup=reply_markup
                )
                return backToHome
        else:
                url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
                websitetronData = requests.post(url)
                tronJsonData = websitetronData.json()
                tronJsonDataData = tronJsonData["data"]
                for teronTxId in tronJsonDataData:
                    if teronTxId["transactionHash"] == update.message.text:
                        if teronTxId["confirmed"] == True:
                            update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                            if int(teronTxId["amount"]) < 202000000 and int(teronTxId["amount"]) > 198000000:
                                update.message.reply_text(
                                  "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                                 ) 
                                time.sleep(2)
                                timestampTime = teronTxId["timestamp"]
                                tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                                tehranTime = str(tehranTime)
                                newDict = {
                                    "amount" : teronTxId["amount"],
                                    "from_address" : teronTxId["transferFromAddress"],
                                    "to_address" : teronTxId["transferToAddress"],
                                    "confirmed" : teronTxId["confirmed"],
                                    "transaction_id" : teronTxId["transactionHash"],
                                    "timestamp" : tehranTime
                                }
                                with open("./teronscan.json" , "r") as teronscanreadingfile:
                                    logData = json.load(teronscanreadingfile)
                                logData.append(newDict)
                                with open("./teronscan.json" , "w") as teronscanwritingfile:
                                    json.dump(logData , teronscanwritingfile , indent = 6)
                                username = update.message.from_user['username']
                                with open("./myfile.json" , "r") as readJsonFile:
                                    jsonFileDicts = json.load(readJsonFile)
                                    historyDict = {
                                                "username" :  update.message.from_user['username'],
                                                "packages" : []
                                            }
                                    print('1')
                                    with open("history.json" , "r") as readinghitoryFile :
                                        historyData = json.load(readinghitoryFile)
                                        if len(historyData) > 0:
                                            print(historyData)
                                            j = 0
                                            for userHistoryData in historyData:
                                                print(userHistoryData)
                                                print('2')
                                                if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                    print('3')
                                                    for i in userHistoryData["packages"]:
                                                      historyDict["packages"].append(i)
                                                    historyData.remove(historyData[j])
                                                    historyDict['packages'].append("اشتراک سه ماهه تریدرزهال")
                                                    historyData.append(historyDict)
                                                    with open("history.json" , "w") as historyJsonFile :
                                                        json.dump(historyData , historyJsonFile , indent = 6)
                                                        break 
                                                j = j + 1    
                                            else:
                                                print('4')
                                                historyDict['packages'].append( "اشتراک یک ساله تریدرزهال")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as writingHistoryFile :
                                                    json.dump(historyData , writingHistoryFile , indent = 6)
                                                        
                                        else:
                                            print('5')
                                            historyDict['packages'].append( "اشتراک یک ساله تریدرزهال")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                    for jsonFiledic in jsonFileDicts:
                                        if jsonFiledic["telegram_id"] == username:
                                            # print(jsonFiledic["user_id"])
                                            uid = jsonFiledic["user_id"]
                                            url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=15"
                                            requests.get(url1)
                                            time.sleep(1)
                                            url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=15"
                                            # 1 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 2 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 3 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 4 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 5 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 6 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 7 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 8 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 9 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 10 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 11 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 12 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            update.message.reply_text(
                                                "✅"
                                                "\n"
                                                "اشتراک یک ساله تریدرزهال  برای شما فعال شد"
                                                "\n"
                                                "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                            ,reply_markup = reply_markup
                                            )
                                return backToHome
                            else:
                                update.message.reply_text(
                                    "⛔️"
                                    "\n"
                                    "مقدار واریزی شما برای این اکانت درست نیست لطفا با پشتیبانی راستاد تماس بگیرید"
                                    "\n"
                                    "@Rastad_Support"
                                ,reply_markup=reply_markup
                                )
                                return backToHome
                else:
                    update.message.reply_text(
                        "⛔️"
                        "\n"
                     "TxId شما پیدا نشد لطفا به پشتیبانی راستاد پیام دهید"
                     "\n"
                     "@Rastad_Support"
                     ,reply_markup=reply_markup
                    )
                    return backToHome
def checkingtxidtraderzhaltwo(update : Update, context: CallbackContext):
    '''in this section checking txid and payment amount for traderhall two month section '''
    print("checkingtxid for traderzhallthree month is run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['برگشت به محصولات']]
    update.message.reply_text(
        "در حال بررسی TxId  لطفا منتظر بمانید..."
        , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    time.sleep(5)
    keyboard = [
        [
          InlineKeyboardButton("بات راستاد", callback_data="1" , url='tg://user?id=382215836'),
    
        ]
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open("./teronscan.json" , "r") as txIdsFile:
        txIds = json.load(txIdsFile)
        for txId in txIds:
            if txId["transaction_id"] == update.message.text:
                update.message.reply_text(
                    "⛔️"
                    "\n"
                   "این Txid قبلا استفاده شده است، اگر نیاز به کمک دارید لطفا به پشتیبانی راستاد پیام دهید:"
                "\n"
                "@Rastad_Support"
                ,reply_markup=reply_markup
                )
                return backToHome
        else:
                url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
                websitetronData = requests.post(url)
                tronJsonData = websitetronData.json()
                tronJsonDataData = tronJsonData["data"]
                for teronTxId in tronJsonDataData:
                    if teronTxId["transactionHash"] == update.message.text:
                        if teronTxId["confirmed"] == True:
                            update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            ,reply_markup=reply_markup
                            )
                            if int(teronTxId["amount"]) < 102000000 and int(teronTxId["amount"]) > 98000000:
                                update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                                time.sleep(2)
                                timestampTime = teronTxId["timestamp"]
                                tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                                tehranTime = str(tehranTime)
                                newDict = {
                                    "amount" : teronTxId["amount"],
                                    "from_address" : teronTxId["transferFromAddress"],
                                    "to_address" : teronTxId["transferToAddress"],
                                    "confirmed" : teronTxId["confirmed"],
                                    "transaction_id" : teronTxId["transactionHash"],
                                    "timestamp" : tehranTime
                                }
                                with open("./teronscan.json" , "r") as teronscanreadingfile:
                                    logData = json.load(teronscanreadingfile)
                                logData.append(newDict)
                                with open("./teronscan.json" , "w") as teronscanwritingfile:
                                    json.dump(logData , teronscanwritingfile , indent = 6)
                                username = update.message.from_user['username']
                                with open("./myfile.json" , "r") as readJsonFile:
                                    jsonFileDicts = json.load(readJsonFile)
                                    historyDict = {
                                                "username" :  update.message.from_user['username'],
                                                "packages" : []
                                            }
                                    print('1')
                                    with open("history.json" , "r") as readinghitoryFile :
                                        historyData = json.load(readinghitoryFile)
                                        if len(historyData) > 0:
                                            print(historyData)
                                            j = 0
                                            for userHistoryData in historyData:
                                                print(userHistoryData)
                                                print('2')
                                                if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                    print('3')
                                                    for i in userHistoryData["packages"]:
                                                      historyDict["packages"].append(i)
                                                    historyData.remove(historyData[j])
                                                    historyDict['packages'].append("اشتراک سه ماهه تریدرزهال")
                                                    historyData.append(historyDict)
                                                    with open("history.json" , "w") as historyJsonFile :
                                                        json.dump(historyData , historyJsonFile , indent = 6)
                                                        break 
                                                j = j + 1    
                                            else:
                                                print('4')
                                                historyDict['packages'].append( "اشتراک سه ماهه تریدرزهال")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as writingHistoryFile :
                                                    json.dump(historyData , writingHistoryFile , indent = 6)
                                                        
                                        else:
                                            print('5')
                                            historyDict['packages'].append( "اشتراک سه ماهه تریدرزهال")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                    for jsonFiledic in jsonFileDicts:
                                        if jsonFiledic["telegram_id"] == username:
                                            # print(jsonFiledic["user_id"])
                                            uid = jsonFiledic["user_id"]
                                            url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=15"
                                            requests.get(url1)
                                            time.sleep(1)
                                            url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=15"
                                            # 1 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 2 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 3 time
                                            requests.get(url2)
                                            update.message.reply_text(
                                                "✅"
                                                "\n"
                                                "اشتراک سه ماهه تریدرزهال  برای شما فعال شد"
                                                "\n"
                                                "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                            ,reply_markup = reply_markup
                                            )
                                return backToHome
                            else:
                                update.message.reply_text(
                                    "⛔️"
                                    "\n"
                                    "مقدار واریزی شما برای این اکانت درست نیست لطفا با پشتیبانی راستاد تماس بگیرید"
                                    "\n"
                     "@Rastad_Support"
                                    ,reply_markup=reply_markup
                                )
                                return backToHome
                else:
                    update.message.reply_text(
                     "TxId شما پیدا نشد لطفا به پشتیبانی راستاد پیام دهید"
                     "\n"
                     "@Rastad_Support"
                     ,reply_markup=reply_markup
                    )
                    return backToHome
def checkingtxidtraderzhalone(update : Update, context: CallbackContext):
    '''in this section checking txid and payment amount for traderhall one month section '''
    print("checkingtxid for traderzhallthree month is run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['برگشت به محصولات']]
    keyboard = [
        [
          InlineKeyboardButton("بات راستاد", callback_data="1" , url='tg://user?id=382215836'),
         
        ]
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "در حال بررسی TxId  لطفا منتظر بمانید..."
         , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    time.sleep(5)
    with open("./teronscan.json" , "r") as txIdsFile:
        txIds = json.load(txIdsFile)
        for txId in txIds:
            if txId["transaction_id"] == update.message.text:
                update.message.reply_text(
                    "⛔️"
                    "\n"
                "این Txid قبلا استفاده شده است، اگر نیاز به کمک دارید لطفا به پشتیبانی راستاد پیام دهید:"
                "\n"
                "@Rastad_Support"
                ,reply_markup=reply_markup
                )
                return backToHome
        else:
                url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
                websitetronData = requests.post(url)
                tronJsonData = websitetronData.json()
                tronJsonDataData = tronJsonData["data"]
                for teronTxId in tronJsonDataData:
                    if teronTxId["transactionHash"] == update.message.text:
                        if teronTxId["confirmed"] == True:
                            update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                            if int(teronTxId["amount"]) < 42000000 and int(teronTxId["amount"]) > 38000000:
                                update.message.reply_text(
                                    "در حال ثبت اشتراک شما در سایت راستاد . لطفا منتظر بمانید ..."
                                
                                )
                                time.sleep(2)
                                timestampTime = teronTxId["timestamp"]
                                tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                                tehranTime = str(tehranTime)
                                newDict = {
                                    "amount" : teronTxId["amount"],
                                    "from_address" : teronTxId["transferFromAddress"],
                                    "to_address" : teronTxId["transferToAddress"],
                                    "confirmed" : teronTxId["confirmed"],
                                    "transaction_id" : teronTxId["transactionHash"],
                                    "timestamp" : tehranTime
                                }
                                with open("./teronscan.json" , "r") as teronscanreadingfile:
                                    logData = json.load(teronscanreadingfile)
                                logData.append(newDict)
                                with open("./teronscan.json" , "w") as teronscanwritingfile:
                                    json.dump(logData , teronscanwritingfile , indent = 6)
                                username = update.message.from_user['username']
                                with open("./myfile.json" , "r") as readJsonFile:
                                    jsonFileDicts = json.load(readJsonFile)
                                    historyDict = {
                                                "username" :  update.message.from_user['username'],
                                                "packages" : []
                                            }
                                    print('1')
                                    with open("history.json" , "r") as readinghitoryFile :
                                        historyData = json.load(readinghitoryFile)
                                        if len(historyData) > 0:
                                            print(historyData)
                                            j = 0
                                            for userHistoryData in historyData:
                                                print(userHistoryData)
                                                print('2')
                                                if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                    print('3')
                                                    for i in userHistoryData["packages"]:
                                                      historyDict["packages"].append(i)
                                                    historyData.remove(historyData[j])
                                                    historyDict['packages'].append("اشتراک یک ماهه تریدرزهال")
                                                    historyData.append(historyDict)
                                                    with open("history.json" , "w") as historyJsonFile :
                                                        json.dump(historyData , historyJsonFile , indent = 6)
                                                        break 
                                                j = j + 1    
                                            else:
                                                print('4')
                                                historyDict['packages'].append( "اشتراک یک ماهه تریدرزهال")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as writingHistoryFile :
                                                    json.dump(historyData , writingHistoryFile , indent = 6)
                                                        
                                        else:
                                            print('5')
                                            historyDict['packages'].append( "اشتراک یک ماهه تریدرزهال")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                    for jsonFiledic in jsonFileDicts:
                                        if jsonFiledic["telegram_id"] == username:
                                            
                                            print("aaaaa")
                                            uid = jsonFiledic["user_id"]
                                            url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=15"
                                            requests.get(url1)
                                            print("bbbbb")
                                            time.sleep(1)
                                            url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=15"
                                            # 1 time
                                            requests.get(url2)
                                            print("ccccc")
                                            update.message.reply_text(
                                                "✅"
                                                "\n"
                                                "اشتراک یک ماهه تریدرزهال  برای شما فعال شد"
                                                "\n"
                                                "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                                
                                            ,reply_markup = reply_markup
                                            )
                                return backToHome
                            else:
                                update.message.reply_text(
                                    "⛔️"
                    "\n"
                                    "مقدار واریزی شما برای این اکانت درست نیست لطفا با پشتیبانی راستاد تماس بگیرید"
                                "\n"
                     "@Rastad_Support"
                                ,reply_markup = reply_markup
                                )
                                return backToHome
                else:
                    update.message.reply_text(
                        "⛔️"
                    "\n"
                     "TxId شما پیدا نشد لطفا به پشتیبانی راستاد پیام دهید"
                     "\n"
                     "@Rastad_Support"
                     ,reply_markup = reply_markup
                    )   
                    return backToHome
def checkingtxidvipone(update : Update, context: CallbackContext):
    '''in this section checking txid and payment amount for vip one month section '''
    print("checkingtxid for traderzhallthree month is run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['برگشت به محصولات']]
    keyboard = [
        [
          InlineKeyboardButton("بات راستاد", callback_data="1" , url='tg://user?id=382215836'),
         
        ]
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "در حال بررسی TxId  لطفا منتظر بمانید..."
         , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    time.sleep(5)
    with open("./teronscan.json" , "r") as txIdsFile:
        txIds = json.load(txIdsFile)
        # print(txIds['transaction_id'])
        for txId in txIds:
            if txId["transaction_id"] == update.message.text:
                update.message.reply_text(
                    "⛔️"
                    "\n"
                   "این Txid قبلا استفاده شده است، اگر نیاز به کمک دارید لطفا به پشتیبانی راستاد پیام دهید:"
               "\n"
                     "@Rastad_Support"
                ,reply_markup= reply_markup
                )
                return backToHome
        else:
                url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
                websitetronData = requests.post(url)
                tronJsonData = websitetronData.json()
                tronJsonDataData = tronJsonData["data"]
                for teronTxId in tronJsonDataData:
                    if teronTxId["transactionHash"] == update.message.text:
                        if teronTxId["confirmed"] == True:
                            update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                            if int(teronTxId["amount"]) < 27000000 and int(teronTxId["amount"]) > 23000000:
                                update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                                time.sleep(2)
                                timestampTime = teronTxId["timestamp"]
                                tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                                tehranTime = str(tehranTime)
                                newDict = {
                                    "amount" : teronTxId["amount"],
                                    "from_address" : teronTxId["transferFromAddress"],
                                    "to_address" : teronTxId["transferToAddress"],
                                    "confirmed" : teronTxId["confirmed"],
                                    "transaction_id" : teronTxId["transactionHash"],
                                    "timestamp" : tehranTime
                                }
                                with open("./teronscan.json" , "r") as teronscanreadingfile:
                                    logData = json.load(teronscanreadingfile)
                                logData.append(newDict)
                                with open("./teronscan.json" , "w") as teronscanwritingfile:
                                    json.dump(logData , teronscanwritingfile , indent = 6)
                                username = update.message.from_user['username']
                                with open("./myfile.json" , "r") as readJsonFile:
                                    jsonFileDicts = json.load(readJsonFile)
                                    historyDict = {
                                                "username" :  update.message.from_user['username'],
                                                "packages" : []
                                            }
                                    print('1')
                                    with open("history.json" , "r") as readinghitoryFile :
                                        historyData = json.load(readinghitoryFile)
                                        if len(historyData) > 0:
                                            print(historyData)
                                            j = 0
                                            for userHistoryData in historyData:
                                                print(userHistoryData)
                                                print('2')
                                                if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                    print('3')
                                                    for i in userHistoryData["packages"]:
                                                      historyDict["packages"].append(i)
                                                    historyData.remove(historyData[j])
                                                    historyDict['packages'].append("اشتراک یک ماهه vip")
                                                    historyData.append(historyDict)
                                                    with open("history.json" , "w") as historyJsonFile :
                                                        json.dump(historyData , historyJsonFile , indent = 6)
                                                        break 
                                                j = j + 1    
                                            else:
                                                print('4')
                                                historyDict['packages'].append("اشتراک یک ماهه vip")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as writingHistoryFile :
                                                    json.dump(historyData , writingHistoryFile , indent = 6)
                                                        
                                        else:
                                            print('5')
                                            historyDict['packages'].append("اشتراک یک ماهه vip")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                    for jsonFiledic in jsonFileDicts:
                                        if jsonFiledic["telegram_id"] == username:
                            
                                            # print(jsonFiledic["user_id"])
                                            uid = jsonFiledic["user_id"]
                                            url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=1"
                                            requests.get(url1)
                                            time.sleep(1)
                                            url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=1"
                                            # 1 time
                                            requests.get(url2)
                                            update.message.reply_text(
                                                "✅"
                                                "\n"
                                                "اشتراک یک ماهه vip برای شما فعال شد"
                                                "\n"
                                                "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                            ,reply_markup = reply_markup
                                            )    
                                return backToHome
                            else:
                                update.message.reply_text(
                                    "⛔️"
                                    "\n"
                                    "مقدار واریزی شما برای این اکانت درست نیست لطفا با پشتیبانی راستاد تماس بگیرید"
                                "\n"
                     "@Rastad_Support"
                                ,reply_markup=reply_markup
                                )
                                return backToHome
                else:
                    update.message.reply_text(
                         "⛔️"
                                    "\n"
                     "TxId شما پیدا نشد لطفا به پشتیبانی راستاد پیام دهید"
                     "\n"
                     "@Rastad_Support"
                     ,reply_markup=reply_markup
                    )  
                    return backToHome
def checkingtxidviptwo(update : Update, context: CallbackContext):
    '''in this section checking txid and payment amount for vip two month section '''
    print("checkingtxid for traderzhallthree month is run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['برگشت به محصولات']]
    keyboard = [
        [
          InlineKeyboardButton("بات راستاد", callback_data="1" , url='tg://user?id=382215836'),
         
        ]
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "در حال بررسی TxId  لطفا منتظر بمانید..."
         , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    time.sleep(5)
    with open("./teronscan.json" , "r") as txIdsFile:
        txIds = json.load(txIdsFile)
        for txId in txIds:
            if txId["transaction_id"] == update.message.text:
                update.message.reply_text(
                     "⛔️"
                                    "\n"
                   "این Txid قبلا استفاده شده است، اگر نیاز به کمک دارید لطفا به پشتیبانی راستاد پیام دهید:"
                "\n"
                "@Rastad_Support"
                ,reply_markup=reply_markup
                )
                return backToHome
        else:
                url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
                websitetronData = requests.post(url)
                tronJsonData = websitetronData.json()
                tronJsonDataData = tronJsonData["data"]
                for teronTxId in tronJsonDataData:
                    if teronTxId["transactionHash"] == update.message.text:
                        if teronTxId["confirmed"] == True:
                            update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                            if int(teronTxId["amount"]) < 72000000 and int(teronTxId["amount"]) > 68000000:
                                update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                                time.sleep(2)
                                timestampTime = teronTxId["timestamp"]
                                tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                                tehranTime = str(tehranTime)
                                newDict = {
                                    "amount" : teronTxId["amount"],
                                    "from_address" : teronTxId["transferFromAddress"],
                                    "to_address" : teronTxId["transferToAddress"],
                                    "confirmed" : teronTxId["confirmed"],
                                    "transaction_id" : teronTxId["transactionHash"],
                                    "timestamp" : tehranTime
                                }
                                with open("./teronscan.json" , "r") as teronscanreadingfile:
                                    logData = json.load(teronscanreadingfile)
                                logData.append(newDict)
                                with open("./teronscan.json" , "w") as teronscanwritingfile:
                                    json.dump(logData , teronscanwritingfile , indent = 6)
                                username = update.message.from_user['username']
                                with open("./myfile.json" , "r") as readJsonFile:
                                    jsonFileDicts = json.load(readJsonFile)
                                    historyDict = {
                                                "username" :  update.message.from_user['username'],
                                                "packages" : []
                                            }
                                    print('1')
                                    with open("history.json" , "r") as readinghitoryFile :
                                        historyData = json.load(readinghitoryFile)
                                        if len(historyData) > 0:
                                            print(historyData)
                                            j = 0
                                            for userHistoryData in historyData:
                                                print(userHistoryData)
                                                print('2')
                                                if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                    print('3')
                                                    for i in userHistoryData["packages"]:
                                                      historyDict["packages"].append(i)
                                                    historyData.remove(historyData[j])
                                                    historyDict['packages'].append("اشتراک دو ماهه vip")
                                                    historyData.append(historyDict)
                                                    with open("history.json" , "w") as historyJsonFile :
                                                        json.dump(historyData , historyJsonFile , indent = 6)
                                                        break 
                                                j = j + 1    
                                            else:
                                                print('4')
                                                historyDict['packages'].append("اشتراک سه ماهه vip")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as writingHistoryFile :
                                                    json.dump(historyData , writingHistoryFile , indent = 6)
                                                        
                                        else:
                                            print('5')
                                            historyDict['packages'].append("اشتراک سه ماهه vip")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                    for jsonFiledic in jsonFileDicts:
                                        if jsonFiledic["telegram_id"] == username:
                                            
                                            # print(jsonFiledic["user_id"])
                                            uid = jsonFiledic["user_id"]
                                            url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=1"
                                            requests.get(url1)
                                            time.sleep(1)
                                            url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=1"
                                            # 1 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 2 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 3 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            update.message.reply_text(
                                                "✅"
                                                "\n"
                                                "اشتراک سه ماهه vip  برای شما فعال شد"
                                                "\n"
                                                "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                            ,reply_markup = reply_markup
                                            )    
                                return backToHome
                            else:
                                update.message.reply_text(
                                     "⛔️"
                                    "\n"
                                    "مقدار واریزی شما برای این اکانت درست نیست لطفا با پشتیبانی راستاد تماس بگیرید"
                                     "\n"
                                     "@Rastad_Support"
                                ,reply_markup=reply_markup
                                )
                                return backToHome
                else:
                    update.message.reply_text(
                         "⛔️"
                                    "\n"
                     "TxId شما پیدا نشد لطفا به پشتیبانی راستاد پیام دهید"
                     "\n"
                     "@Rastad_Support"
                     ,reply_markup=reply_markup
                    )            
                    return backToHome
def checkingtxidvipthree(update : Update, context: CallbackContext):
    '''in this section checking txid and payment amount for vip three month section '''
    print("checkingtxid for traderzhallthree month is run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    reply_keyboard = [['برگشت به محصولات']]
    keyboard = [
        [
          InlineKeyboardButton("بات راستاد", callback_data="1" , url='tg://user?id=382215836'),
          
        ]
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "در حال بررسی TxId  لطفا منتظر بمانید..."
         , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    time.sleep(5)
    with open("./teronscan.json" , "r") as txIdsFile:
        txIds = json.load(txIdsFile)
        for txId in txIds:
            if txId["transaction_id"] == update.message.text:
                update.message.reply_text(
                     "⛔️"
                                    "\n"
                   "این Txid قبلا استفاده شده است، اگر نیاز به کمک دارید لطفا به پشتیبانی راستاد پیام دهید:"
                "\n"
                "@Rastad_Support"
                
                )
                return backToHome
        else:
                url = "https://apilist.tronscan.org/api/contract/events?address=TDtxsMUNmta7tAQ84vSkV6N4Z3Xi3F4LAf&limit=100000000"
                websitetronData = requests.post(url)
                tronJsonData = websitetronData.json()
                tronJsonDataData = tronJsonData["data"]
                for teronTxId in tronJsonDataData:
                    if teronTxId["transactionHash"] == update.message.text:
                        if teronTxId["confirmed"] == True:
                            update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            ,reply_markup=reply_markup
                            )
                            if int(teronTxId["amount"]) < 152000000 and int(teronTxId["amount"]) > 148000000:
                                update.message.reply_text(
                            "پرداخت شما با موفقیت انجام شد در حال بررسی مقدار واریزی ..."
                            )
                                time.sleep(2)
                                timestampTime = teronTxId["timestamp"]
                                tehranTime = datetime.datetime.utcfromtimestamp(timestampTime / 1e3)
                                tehranTime = str(tehranTime)
                                newDict = {
                                    "amount" : teronTxId["amount"],
                                    "from_address" : teronTxId["transferFromAddress"],
                                    "to_address" : teronTxId["transferToAddress"],
                                    "confirmed" : teronTxId["confirmed"],
                                    "transaction_id" : teronTxId["transactionHash"],
                                    "timestamp" : tehranTime
                                }
                                with open("./teronscan.json" , "r") as teronscanreadingfile:
                                    logData = json.load(teronscanreadingfile)
                                logData.append(newDict)
                                with open("./teronscan.json" , "w") as teronscanwritingfile:
                                    json.dump(logData , teronscanwritingfile , indent = 6)
                                username = update.message.from_user['username']
                                with open("./myfile.json" , "r") as readJsonFile:
                                    jsonFileDicts = json.load(readJsonFile)
                                    historyDict = {
                                                "username" :  update.message.from_user['username'],
                                                "packages" : []
                                            }
                                    print('1')
                                    with open("history.json" , "r") as readinghitoryFile :
                                        historyData = json.load(readinghitoryFile)
                                        if len(historyData) > 0:
                                            print(historyData)
                                            j = 0
                                            for userHistoryData in historyData:
                                                print(userHistoryData)
                                                print('2')
                                                if str(userHistoryData['username']) == str(update.message.from_user['username']):
                                                    print('3')
                                                    for i in userHistoryData["packages"]:
                                                      historyDict["packages"].append(i)
                                                    historyData.remove(historyData[j])
                                                    historyDict['packages'].append("اشتراک یک ساله vip")
                                                    historyData.append(historyDict)
                                                    with open("history.json" , "w") as historyJsonFile :
                                                        json.dump(historyData , historyJsonFile , indent = 6)
                                                        break 
                                                j = j + 1    
                                            else:
                                                print('4')
                                                historyDict['packages'].append("اشتراک یک ساله vip")
                                                historyData.append(historyDict)
                                                with open("history.json" , "w") as writingHistoryFile :
                                                    json.dump(historyData , writingHistoryFile , indent = 6)
                                                        
                                        else:
                                            print('5')
                                            historyDict['packages'].append("اشتراک یک ساله vip")
                                            historyData.append(historyDict)
                                            with open("history.json" , "w") as writingHistoryFile :
                                                json.dump(historyData , writingHistoryFile , indent = 6)
                                    for jsonFiledic in jsonFileDicts:
                                        if jsonFiledic["telegram_id"] == username:
                                            historyDict = {
                                                "username" :  update.message.from_user['username'],
                                                "packages" : []
                                            }
                                            with open("history.json" , "r") as readinghitoryFile :
                                                historyData = json.load(readinghitoryFile)
                                                for userHistoryData in historyData:
                                                    if userHistoryData['username'] == update.message.from_user['username']:
                                                        userHistoryData['packages'].append("اشتراک یک ساله vip")
                                                        with open("history.json" , "w") as historyJsonFile :
                                                            json.dump(userHistoryData , historyJsonFile , indent = 6)
                                                    else:
                                                        historyDict['packages'].append("اشتراک یک ساله vip")
                                                        with open("history.json" , "w") as writingHistoryFile :
                                                            json.dump(historyDict , writingHistoryFile , indent = 6)
                                            # print(jsonFiledic["user_id"])
                                            uid = jsonFiledic["user_id"]
                                            url1 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_add_level&uid={uid}&lid=1"
                                            requests.get(url1)
                                            time.sleep(1)
                                            url2 = f"https://smrastad.com/wp-content/plugins/indeed-membership-pro/apigate.php?ihch=7hfebhWCkjsN2GdiwdmKi1b2zv8fmbWl&action=user_activate_level&uid={uid}&lid=1"
                                            # 1 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 2 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 3 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 4 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 5 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 6 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 7 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 8 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 9 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 10 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 11 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            # 12 time
                                            requests.get(url2)
                                            time.sleep(1)
                                            update.message.reply_text(
                                                "✅"
                                                "\n"
                                                "اشتراک یک ساله vip راستاد برای شما فعال شد"
                                                "\n"
                                                "برای دریافت لینک ورود، توسط دکمه زیر به بات راستاد بروید.""\n""اگر به مشکلی برخوردید به پشتیبانی راستاد پیام دهید: @Rastad_Support"
                                            ,reply_markup = reply_markup
                                            )
                                return backToHome
                            else:
                                update.message.reply_text(
                                    "⛔️"
                                    "\n"
                                    "مقدار واریزی شما برای این اکانت درست نیست لطفا با پشتیبانی راستاد تماس بگیرید"
                                    "\n"
                     "@Rastad_Support"
                                    ,reply_markup=reply_markup
                                )
                                return backToHome
                else:
                    update.message.reply_text(
                        "⛔️"
                                    "\n"
                     "TxId شما پیدا نشد لطفا به پشتیبانی راستاد پیام دهید"
                     "\n"
                     "@Rastad_Support"
                     ,reply_markup=reply_markup
                    ) 
                    return backToHome
def cancel(update: Update, context: CallbackContext) -> int:
    '''when user send /cancel this section started'''
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    print("cancel run")
    reply_keyboard = [['شروع دوباره']]
    update.message.reply_text(
        "ممنون که ما را انتخاب کردید "
        "\n"
        "درصورت شروع دوباره روی دکمه ی پایین کلیک کنید"
        , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True , resize_keyboard=True)
    )
    return cancelbut
def startagain(update: Update, context: CallbackContext) -> int:
    print("start again is run")
    bot.send_chat_action(chat_id=update.message.from_user['id'], action=telegram.ChatAction.TYPING)
    username = update.message.from_user['username']
    if username == None:    
            update.message.reply_text(
                "شما username telegram  ندارید ، لطفا از طریق setting telegram یک  username  برای خود بسازید و سپس روی دکمه ی 'start'در پایین بزنید"
            )
            return ConversationHandler.END
    else:
            update.message.reply_text(
            "لطفا منتظر بمانید ، در حال اتصال به سایت راستاد ..."
            )
            time.sleep(3)
            return newperm(update , context)

def main() :
    '''main section , mother of functions :D  , bot keep run and state was run in this section'''
    updater = Updater("1792099185:AAHfOO8OtkIbbue050qm9kBl70yQzS_NgNc")
    dispatcher = updater.dispatcher
    
    conv_handler = ConversationHandler(
        entry_points=[
        CommandHandler('start', start),
        ],
        states = {
            newpermission: [MessageHandler(Filters.text & ~Filters.command, newperm)],
            cancelbut:[MessageHandler(Filters.regex('^(شروع دوباره)$'), newperm)],
           
            packages:[
                MessageHandler(Filters.regex('^(راستاد VIP)$'), vipRastad),
                MessageHandler(Filters.regex('^(Traders Hall)$'), traderhall),
                MessageHandler(Filters.regex('^(لغو درخواست)$'), cancel),
                ],
            aftervip : [
                MessageHandler(Filters.regex('^(یک ماهه 25 دلار)$'), howtopayvip1),
                MessageHandler(Filters.regex('^(سه ماهه 70 دلار)$'), howtopayvip2),
                MessageHandler(Filters.regex('^(یک ساله 150 دلار)$'), howtopayvip3),
                MessageHandler(Filters.regex('^(برگشت به انتخاب اشتراک ها)$'), howtopayvip3),
            ],
            AssetVip1 : [
                MessageHandler(Filters.regex('^(کیف پول)$'), assetvip1),
                MessageHandler(Filters.regex('^(Txid)$'), viponemonth),
                MessageHandler(Filters.regex('^(لغو درخواست)$'), newperm),
            ],
            AssetVip2 : [
                MessageHandler(Filters.regex('^(کیف پول)$'), assetvip2),
                MessageHandler(Filters.regex('^(Txid)$'), viptwomonth),
                MessageHandler(Filters.regex('^(لغو درخواست)$'), newperm),
            ],
            AssetVip3 : [
                MessageHandler(Filters.regex('^(کیف پول)$'), assetvip3),
                MessageHandler(Filters.regex('^(Txid)$'), vipthreemonth),
                MessageHandler(Filters.regex('^(لغو درخواست)$'), newperm),
            ],
            CheckQrCodeVip1:[
                MessageHandler(Filters.text & ~Filters.command, checkingQRcodevip1)
            ],
            CheckQrCodeVip2:[
                MessageHandler(Filters.text & ~Filters.command, checkingQRcodevip2)
            ],
            CheckQrCodeVip3:[
                MessageHandler(Filters.text & ~Filters.command, checkingQRcodevip3)
            ],
            CheckAssetVip1 : [
                MessageHandler(Filters.text & ~Filters.command, checkingassetvip1)
            ],
            CheckAssetVip2 : [
                MessageHandler(Filters.text & ~Filters.command, checkingassetvip2)
            ],
            CheckAssetVip3 : [
                MessageHandler(Filters.text & ~Filters.command, checkingassetvip3)
            ],
            aftertraderzhal:[
                MessageHandler(Filters.regex('^(برگشت به انتخاب اشتراک ها)$'), newperm),
                MessageHandler(Filters.regex('^(یک ماهه 40 دلار)$'), howtopayth1),
                MessageHandler(Filters.regex('^(سه ماهه 100 دلار)$'), howtopayth2),
                MessageHandler(Filters.regex('^(یک ساله 200 دلار)$'), howtopayth3),
            ],
            AssetTh1 : [
                MessageHandler(Filters.regex('^(کیف پول)$'), assetTh1),
                MessageHandler(Filters.regex('^(Txid)$'), traderzhalonemonth),
                MessageHandler(Filters.regex('^(لغو درخواست)$'), newperm),
            ],
            AssetTh2 : [
                MessageHandler(Filters.regex('^(کیف پول)$'), assetTh2),
                MessageHandler(Filters.regex('^(Txid)$'), traderzhaltwomonth),
                MessageHandler(Filters.regex('^(لغو درخواست)$'), newperm),
            ],
            AssetTh3 : [
                MessageHandler(Filters.regex('^(کیف پول)$'), assetTh3),
                MessageHandler(Filters.regex('^(Txid)$'), traderzhalthreemonth),
                MessageHandler(Filters.regex('^(لغو درخواست)$'), newperm),
            ],
            CheckQrCodeTh1:[
                MessageHandler(Filters.text & ~Filters.command, checkingQRcodeTh1)
            ],
            CheckQrCodeTh2:[
                MessageHandler(Filters.text & ~Filters.command, checkingQRcodeTh2)
            ],
            CheckQrCodeTh3:[
                MessageHandler(Filters.text & ~Filters.command, checkingQRcodeTh3)
            ],
            CheckAssetTh1 : [
                MessageHandler(Filters.text & ~Filters.command, checkingassetTh1)
            ],
            CheckAssetTh2 : [
                MessageHandler(Filters.text & ~Filters.command, checkingassetTh2)
            ],
            CheckAssetTh3 : [
                MessageHandler(Filters.text & ~Filters.command, checkingassetTh3)
            ],
            checktxidtraderhallthree :[
                MessageHandler(Filters.text & ~Filters.command, checkingtxidtraderzhalthree)
            ],
            checktxidtraderhalltwo :[
                MessageHandler(Filters.text & ~Filters.command, checkingtxidtraderzhaltwo)
            ],
            checktxidtraderhallone :[
                MessageHandler(Filters.text & ~Filters.command, checkingtxidtraderzhalone)
            ],
            checkvipone :[
                MessageHandler(Filters.text & ~Filters.command, checkingtxidvipone)
            ],
            checkviptwo :[
                MessageHandler(Filters.text & ~Filters.command, checkingtxidviptwo)
            ],
            checkvipthree :[
                MessageHandler(Filters.text & ~Filters.command, checkingtxidvipthree)
            ],
            backToHome:[
                MessageHandler(Filters.regex('^(برگشت به محصولات)$'), startagain),
            ],
            # checkassetvip1 : [MessageHandler(Filters.text & ~Filters.command, checkingassetvip1)],
            
        },
        fallbacks=[CommandHandler('cancel', cancel),],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
    


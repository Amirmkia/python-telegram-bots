import ccxt
import json 
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import datetime
import time
from datetime import date
from datetime import timedelta
print("I'm Ready")

def priceAlert():
    print("I'm Ready on Function")
    with open("./Data.json" , "r") as readingDataFile:
        signals = json.load(readingDataFile)
        if len(signals) >0 :
            for signal in signals:
                if signal['confirmed'] == 0:
                    spot = signal["spot"].split(" ")
                    if spot[1] =="Spot":
                        exchange = signal["spot"].split(" ")
                        exchangeCoin = exchange[0]
                        method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                        exchange_obj = method_to_call()
                        pair_price_data = exchange_obj.fetch_ticker(signal["name"])
                        closing_price = pair_price_data['close']
                        E1 = float(signal["enter_price"][0])
                        E2 = float(signal["enter_price"][1])
                        enter_price = (E1 + E2)/2
                        if float(closing_price) < float(enter_price):
                            with open("./Data.json" , "w") as writingSignalFile:
                                signal["enter_price_launched"] = 1
                                json.dump(signals , writingSignalFile , indent=6)
                        print("signal is long Spot")
                        if signal["enter_price_launched"] == 0:
                            print("in Flase")
                            exchange = signal["spot"].split(" ")
                            exchangeCoin = exchange[0]
                            method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                            exchange_obj = method_to_call()
                            pair_price_data = exchange_obj.fetch_ticker(signal["name"])
                            closing_price = pair_price_data['close']
                            print("coin price : " + str(closing_price))
                            if signal["timing"] == "D":
                                today = date.today()
                                tomorrow = today + timedelta(days = 1)
                                yesterday = today - timedelta(days = 1)
                                print("Yesterday was: ", yesterday)
                                print("signal date: " + signal['date'])
                                if str(signal["date"]) == str(yesterday):
                                    print("salam")
                                    timestamp = int(datetime.datetime.strptime(f"{today} 3:29:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
                                    binance = signal['spot'].split(" ")
                                    exchange = str(binance[0])
                                    exchangeCoin = exchange
                                    method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                                    exchange_obj = method_to_call()
                                    recponce = exchange_obj.fetch_ohlcv(str(signal['name']), '1m', timestamp, 1)
                                    rec = responce[0]
                                    price = rec[4]
                                    if float(price) <= float(signal['stop']):
                                        print("stop in daily Done")
                                        channel = "-681209528"
                                        sl = float(signal['stop'])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((E - sl)/E) * 100
                                        bot_message = f"{signal['name']}" + "\n" +  f"Loss : {profit}%" + "\n" + "Stopped out ⛔️"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingSignalFile:
                                            signal['loss'] = profit
                                            signal['confirmed'] = 1 
                                            json.dump(signals , writingDataFile , indent = 6)
                                    elif float(closing_price) <= float(signal["enter_price"][1]):
                                        print("signal has been launched")
                                        print(signal)
                                        bot_message = f"{signal['name']}" + "\n" + "EnterPrice Reached ✅"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingSignalFile:
                                            signal["enter_price_launched"] = 1
                                            json.dump(signals , writingSignalFile , indent = 6)
                            if signal['timing'] == "N":
                                if float(closing_price) <= float(signal["stop"]):
                                    print("Signall stoped out")
                                    channel = "-681209528"
                                    sl = float(signal['stop'])
                                    E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                    profit = ((E - sl)/E) * 100
                                    bot_message = f"{signal['name']}" + "\n" +  f"Loss : {profit}%" + "\n" + "Stopped out ⛔️"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingDataFile:
                                        signal["confirmed"] = 1
                                        signal['loss'] = profit
                                        json.dump(signals , writingDataFile , indent = 6)
                                        # break
                                elif float(closing_price) <= float(signal["enter_price"][1]):
                                    print("signal has been launched")
                                    print(signal)
                                    bot_message = f"{signal['name']}" + "\n" + "EnterPrice Reached ✅"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingSignalFile:
                                        signal["enter_price_launched"] = 1
                                        json.dump(signals , writingSignalFile , indent = 6)
                                timestamp = int(datetime.datetime.strptime(f"{today} 3:29:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
                                exchange = "Binance"
                                exchangeCoin = exchange
                                method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                                exchange_obj = method_to_call()
                                response = exchange_obj.fetch_ohlcv(str(signal['name']), '1m', timestamp, 1)
                                print(response)
                        if signal["enter_price_launched"] == 1:
                            print("in True")
                            #len=1
                            if len(signal["targets"]) == 1:
                                if float(closing_price) >= float(signal["targets"][0]):
                                    print("Target(1) Reached and signal fully closed")
                                    tp = float(signal['targets'][0])
                                    E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                    profit = ((tp - E)/E) * 100
                                    signal_day = signal['time'].split("-")
                                    day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                    day_now = str(date.today()).split("-")
                                    day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                    difference = day_two - day_one
                                    profit = round(profit , 2)
                                    bot_message = f"{signal['name']}(LONG) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingDataFile:
                                        signal["target1"] = 1
                                        signal["confirmed"] = 1
                                        signal['profit'] = profit
                                        json.dump(signals , writingDataFile , indent = 6)
                            #len = 2
                            if len(signal["targets"]) == 2:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(2) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target2(2) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)

                            #len = 3 
                            if len(signal["targets"]) == 3:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target2(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) <= float(closing_price):
                                        print("target3(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            #len = 4
                            if len(signal["targets"]) == 4:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target2(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) <= float(closing_price):
                                        print("target3(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][1]
                                if signal["target4"] == 0:
                                    if float(signal["targets"][4]) <= float(closing_price):
                                        print("signal 4 (4) is launched")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][3])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target4 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target4"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            #len = 5
                            if len(signal["targets"]) == 5:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target2(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) <= float(closing_price):
                                        print("target3(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][1]
                                if signal["target4"] == 0:
                                    if float(signal["targets"][4]) <= float(closing_price):
                                        print("signal 4 (5) is launched")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][3])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target4 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target4"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][2]
                                if signal["target5"] == 0:
                                    if float(closing_price) >= float(signal["targets"][4]):
                                        print("All targets(5) reached and signal fully closed")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][4])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((tp - E)/E) * 100
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG) \n Target5 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target5"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            print("nothing launched")
                    short = signal["spot"].split(" ") 
                    print(short)
                    print(len(short))
                    if signal["spot"] == "Binance Futures (SHORT)":
                        print("signal is short") 
                        exchange = signal["spot"].split(" ")
                        exchangeCoin = exchange[0]
                        method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                        exchange_obj = method_to_call()
                        pair_price_data = exchange_obj.fetch_ticker(signal["name"])
                        closing_price = pair_price_data['close'] 
                        E1 = float(signal["enter_price"][0])
                        E2 = float(signal["enter_price"][1])
                        enter_price = (E1 + E2)/2
                        if float(closing_price) > float(enter_price):
                            with open("./Data.json" , "w") as writingSignalFile:
                                signal["enter_price_launched"] = 1
                                json.dump(signals , writingSignalFile , indent = 6) 
                        if signal["enter_price_launched"] == 0:
                            print("in Flase")
                            if signal["timing"] == "N":
                                exchange = signal["spot"].split(" ")
                                exchangeCoin = exchange[0]
                                method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                                exchange_obj = method_to_call()
                                pair_price_data = exchange_obj.fetch_ticker(signal["name"])
                                closing_price = pair_price_data['close']
                                print("coin price : " + str(closing_price))
                                if float(closing_price) >= float(signal["stop"]):
                                    print("Signal stoped out")
                                    channel = "-681209528"
                                    sl = float(signal['stop'])
                                    E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                    profit = float(((sl - E)/E) * 100) * float(signal['lev_futures'])
                                    bot_message = f"{signal['name']}" + "\n" +  f"Loss : {profit}%" + "\n" + "Stopped out ⛔️"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingDataFile:
                                        signal["confirmed"] = 1
                                        signal['loss'] = profit
                                        json.dump(signals , writingDataFile , indent = 6)
                                        # break
                                elif float(closing_price) <= float(signal["enter_price"][1]):
                                    print("signal has been launched")
                                    print(signal)
                                    #-------------
                                    bot_message = f"{signal['name']}" + "\n" + "EnterPrice Reached ✅"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    #-------------
                                    with open("./Data.json" , "w") as writingSignalFile:
                                        signal["enter_price_launched"] = 1
                                        json.dump(signals , writingSignalFile , indent = 6)    
                            if signal["timing"] == "D":
                                today = date.today()
                                tomorrow = today + timedelta(days = 1)
                                yesterday = today - timedelta(days = 1)
                                print("Yesterday was: ", yesterday)
                                print("signal date: " + signal['date'])
                                if str(signal["date"]) == str(yesterday):
                                    print("salam")
                                    timestamp = int(datetime.datetime.strptime(f"{today} 3:29:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
                                    binance = signal['spot'].split(" ")
                                    exchange = str(binance[0])
                                    exchangeCoin = exchange
                                    method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                                    exchange_obj = method_to_call()
                                    responce = exchange_obj.fetch_ohlcv(str(signal['name']), '1m', timestamp, 1)
                                    rec = responce[0]
                                    price = rec[4]
                                    if float(price) >= float(signal['stop']):
                                        print("stop in daily Done")
                                        channel = "-681209528"
                                        sl = float(signal['stop'])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((E - sl)/E) * 100
                                        bot_message = f"{signal['name']}" + "\n" +  f"Loss : {profit}%" + "\n" + "Stopped out ⛔️"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingSignalFile:
                                            signal['confirmed'] = 1 
                                            signal['loss'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                    elif float(closing_price) <= float(signal["enter_price"][1]):
                                        print("signal has been launched")
                                        print(signal)
                                        bot_message = f"{signal['name']}" + "\n" + "EnterPrice Reached ✅"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingSignalFile:
                                            signal["enter_price_launched"] = 1
                                            json.dump(signals , writingSignalFile , indent = 6)
                        if signal["enter_price_launched"] == 1:
                            print("in True")
                            #len = 1
                            print("len signal : " + str(len(signal['targets'])))
                            if len(signal["targets"]) == 1:
                                if float(closing_price) <= float(signal["targets"][0]):
                                    print("Target(1) Reached and signal fully closed")
                                    channel = "-681209528"
                                    tp = float(signal['targets'][0])
                                    E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                    profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                    signal_day = signal['time'].split("-")
                                    day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                    day_now = str(date.today()).split("-")
                                    day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                    difference = day_two - day_one
                                    profit = round(profit , 2)
                                    bot_message = f"{signal['name']}(SHORT) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingDataFile:
                                        signal["target1"] = 1
                                        signal["confirmed"] = 1
                                        json.dump(signals , writingDataFile , indent = 6)
                            #len = 2
                            if len(signal["targets"]) == 2:
                                if signal["target1"] == 0:
                                    if float(closing_price) <= float(signal["targets"][0]):
                                        print("target1(2) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) >= float(closing_price):
                                        print("target2(2) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)

                            #len = 3 
                            if len(signal["targets"]) == 3:
                                if signal["target1"] == 0:
                                    if float(closing_price) <= float(signal["targets"][0]):
                                        print("target1(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) >= float(closing_price):
                                        print("target2(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) >= float(closing_price):
                                        print("target3(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            #len = 4
                            if len(signal["targets"]) == 4:
                                if signal["target1"] == 0:
                                    if float(closing_price) <= float(signal["targets"][0]):
                                        print("target1(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) >= float(closing_price):
                                        print("target2(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) >= float(closing_price):
                                        print("target3(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][1]
                                if signal["target4"] == 0:
                                    if float(signal["targets"][4]) >= float(closing_price):
                                        print("signal 4 (4) is launched")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][3])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target4"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                
                            #len = 5
                            if len(signal["targets"]) == 5:
                                if signal["target1"] == 0:
                                    if float(closing_price) <= float(signal["targets"][0]):
                                        print("target1(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) >= float(closing_price):
                                        print("target2(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) >= float(closing_price):
                                        print("target3(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][1]
                                if signal["target4"] == 0:
                                    if float(signal["targets"][4]) >= float(closing_price):
                                        print("signal 4 (5) is launched")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][3])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target4 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target4"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][2]
                                if signal["target5"] == 0:
                                    if float(closing_price) <= float(signal["targets"][4]):
                                        print("All targets(5) reached and signal fully closed")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][4])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((E - tp)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(SHORT) \n Target5 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target5"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            print("nothing launched")
                    spot = signal["spot"].split(" ")
                    if signal["spot"] == "Binance Futures (LONG)":
                        exchange = signal["spot"].split(" ")
                        exchangeCoin = exchange[0]
                        method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                        exchange_obj = method_to_call()
                        pair_price_data = exchange_obj.fetch_ticker(signal["name"])
                        closing_price = pair_price_data['close']
                        E1 = float(signal["enter_price"][0])
                        E2 = float(signal["enter_price"][1])
                        enter_price = (E1 + E2)/2
                        if float(closing_price) < float(enter_price):
                            with open("./Data.json" , "w") as writingSignalFile:
                                signal["enter_price_launched"] = 1
                                json.dump(signals , writingSignalFile , indent = 6)
                        print("signal is long Futures")
                        if signal["enter_price_launched"] == 0:
                            print("in Flase")
                            if signal["timing"] == "D":
                                today = date.today()
                                tomorrow = today + timedelta(days = 1)
                                yesterday = today - timedelta(days = 1)
                                print("Yesterday was: ", yesterday)
                                print("signal date: " + signal['date'])
                                if str(signal["date"]) == str(yesterday):
                                    print("salam")
                                    timestamp = int(datetime.datetime.strptime(f"{today} 3:29:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
                                    binance = signal['spot'].split(" ")
                                    exchange = str(binance[0])
                                    exchangeCoin = exchange
                                    method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                                    exchange_obj = method_to_call()
                                    recponce = exchange_obj.fetch_ohlcv(str(signal['name']), '1m', timestamp, 1)
                                    rec = responce[0]
                                    price = rec[4]
                                    if float(price) <= float(signal['stop']):
                                        print("stop in daily Done")
                                        channel = "-681209528"
                                        sl = float(signal['stop'])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = ((E - sl)/E) * 100
                                        bot_message = f"{signal['name']}" + "\n" +  f"Loss : {profit}%" + "\n" + "Stopped out ⛔️"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingSignalFile:
                                            signal['confirmed'] = 1 
                                            signal['loss'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                    elif float(closing_price) <= float(signal["enter_price"][1]):
                                        print("signal has been launched")
                                        print(signal)
                                        bot_message = f"{signal['name']}" + "\n" + "EnterPrice Reached ✅"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingSignalFile:
                                            signal["enter_price_launched"] = 1
                                            json.dump(signals , writingSignalFile , indent = 6)
                            if signal['timing'] == "N":
                                exchange = signal["spot"].split(" ")
                                exchangeCoin = exchange[0]
                                method_to_call = getattr(ccxt,exchangeCoin.lower()) 
                                exchange_obj = method_to_call()
                                pair_price_data = exchange_obj.fetch_ticker(signal["name"])
                                closing_price = pair_price_data['close']
                                print("coin price : " + str(closing_price))
                                E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                if float(closing_price) <= float(signal["stop"]):
                                    print("Signall stoped out")
                                    channel = "-681209528"
                                    sl = float(signal['stop'])
                                    E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                    profit = float(((E - sl)/E) * 100) * float(signal['lev_futures'])
                                    bot_message = f"{signal['name']}" + "\n" +  f"Loss : {profit}%" + "\n" + "Stopped out ⛔️"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingDataFile:
                                        signal["confirmed"] = 1
                                        signal['loss'] = profit
                                        json.dump(signals , writingDataFile , indent = 6)
                                        # break
                                elif float(closing_price) >= float(E):
                                    print("signal has been launched")
                                    print(signal)
                                    bot_message = f"{signal['name']}" + "\n" + "EnterPrice Reached ✅"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingSignalFile:
                                        signal["enter_price_launched"] = 1
                                        json.dump(signals , writingSignalFile , indent = 6)
                        if signal["enter_price_launched"] == 1:
                            print("in True")
                            #len = 1 
                            if len(signal["targets"]) == 1:
                                if float(closing_price) >= float(signal["targets"][0]):
                                    print("Target(1) Reached and signal fully closed")
                                    channel = "-681209528"
                                    tp = float(signal['targets'][0])
                                    E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                    profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                    signal_day = signal['time'].split("-")
                                    day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                    day_now = str(date.today()).split("-")
                                    day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                    difference = day_two - day_one
                                    profit = round(profit , 2)
                                    bot_message = f"{signal['name']}(LONG FUTURES) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                    bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                    channel = "-738934496"
                                    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                    header = {
                                        "reply_to_message_id" : int(signal['messageId']),
                                        "parse_mode" : "Markdown" ,
                                        "text" : bot_message
                                    }
                                    requests.post(send_text , json= header)
                                    with open("./Data.json" , "w") as writingDataFile:
                                        signal["target1"] = 1
                                        signal["confirmed"] = 1
                                        signal['profit'] = profit
                                        json.dump(signals , writingDataFile , indent = 6)
                            #len = 2
                            if len(signal["targets"]) == 2:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(2) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target2(2) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)

                            #len = 3 
                            if len(signal["targets"]) == 3:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target2(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) <= float(closing_price):
                                        print("target3(3) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            #len = 4
                            if len(signal["targets"]) == 4:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target2(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][3]) <= float(closing_price):
                                        print("target3(4) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][1]
                                if signal["target4"] == 0:
                                    if float(signal["targets"][4]) <= float(closing_price):
                                        print("signal 4 (4) is launched")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][3])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target4 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target4"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            #len = 5
                            if len(signal["targets"]) == 5:
                                if signal["target1"] == 0:
                                    if float(closing_price) >= float(signal["targets"][0]):
                                        print("target1(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][0])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target1 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target1"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            enterprice = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                            signal['stop'] = enterprice
                                if signal["target2"] == 0:
                                    if float(signal["targets"][1]) <= float(closing_price):
                                        print("target2(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][1])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target2 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target2"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][0]
                                if signal["target3"] == 0:
                                    if float(signal["targets"][2]) <= float(closing_price):
                                        print("target3(5) reached")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][2])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target3 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target3"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][1]
                                if signal["target4"] == 0:
                                    if float(signal["targets"][3]) <= float(closing_price):
                                        print("signal 4 (5) is launched")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][3])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target4 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target4"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                                        if signal['ts'] == 1:
                                            signal['stop'] = signal['targets'][2] 
                                if signal["target5"] == 0:
                                    if float(closing_price) >= float(signal["targets"][4]):
                                        print("All targets(5) reached and signal fully closed")
                                        channel = "-681209528"
                                        tp = float(signal['targets'][4])
                                        E = (float(signal['enter_price'][0]) + float(signal['enter_price'][1]))/2
                                        profit = float(((tp - E)/E) * 100) * float(signal['lev_futures'])
                                        signal_day = signal['time'].split("-")
                                        day_one = date(int(signal_day[0]) , int(signal_day[1]), int(signal_day[2]))
                                        day_now = str(date.today()).split("-")
                                        day_two = date(int(day_now[0]) , int(day_now[1]) , int(day_now[2]))
                                        difference = day_two - day_one
                                        profit = round(profit , 2)
                                        bot_message = f"{signal['name']}(LONG FUTURES) \n Target5 Reached✅ \n profit : {profit}% 🔥 \n 🗓{signal['time']} \n Period: {difference}"
                                        bot_token = "5177794563:AAE-I8ZhJ1nfriaoBCyws0A89oq7oKL0wbA"
                                        channel = "-738934496"
                                        send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + channel
                                        header = {
                                            "reply_to_message_id" : int(signal['messageId']),
                                            "parse_mode" : "Markdown" ,
                                            "text" : bot_message
                                        }
                                        requests.post(send_text , json= header)
                                        with open("./Data.json" , "w") as writingDataFile:
                                            signal["target5"] = 1
                                            signal["confirmed"] = 1
                                            signal['profit'] = profit
                                            json.dump(signals , writingDataFile , indent = 6)
                            print("nothing launched")
                else:
                    print("signal is confirmed")
            
 
# priceAlert()
scheduler = BlockingScheduler()
scheduler.add_job(priceAlert, 'interval', hours=0.008)
scheduler.start()

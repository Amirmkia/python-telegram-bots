API_KEY=""
API_URL = f"https://api.telegram.org/bot{API_KEY}"+'/{metho}'
import pandas as pd
import json
import os
from telegram import *
from telegram.ext import *



class bot:
  def __init__(self,load_address="result.txt",do_load=True):
    self.questions=pd.DataFrame({"question":[
      "درخواست مرخصی جدید",
      "مشاهده درخواست ها"
      ],
    "options":[{0:"بلی",1:"خیر",2:"تا حدودی "},{0:"بلی",1:"خیر",2:"تا حدودی "},],"number_of_options":[3,3],"type":["mo","mo"]})
    self.users={}
    self.load_address=load_address
    if os.path.exists(self.load_address) and do_load:
      #print("path exists")
      self.users=self.load_result()
    self.updater=telegram.ext.Updater(API_KEY,use_context=True)
    self.dp=self.updater.dispatcher
    self.dp.add_handler(telegram.ext.CommandHandler("start",self.start_command))
    self.dp.add_handler(telegram.ext.CallbackQueryHandler(self.handle_button))
    self.dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,self.handle_message))
    self.updater.start_polling()
    self.updater.idle()

  def start_command(self,update, context):
      id = str(update.message.from_user.username)
      idnum = str(update.message.from_user.username)
      if id in self.users.keys():
        if id=="Amirm_1376":
           with open("result.txt", "rb") as file:
            context.bot.send_document(chat_id=382215836, document=file,  
            filename='result.txt')
        else:
             app.client.update.message.reply_text("ممنون ولی شما در نظرسنجی ما شرکت کرده اید .")
      else:    
        self.users[id]={"id":id,"question":0,"answers":[],"question_shown":False}
        self.question(update,context)
        #keyboard=[[telegram.InlineKeyboardButton(f"بپرس", callback_data=f'بپرس')]]
        #reply_markup=telegram.InlineKeyboardMarkup(keyboard)
        #update.message.reply_text("میخوای به چند تا سوال جواب بدی ؟",reply_markup=reply_markup)



  def create_button(self,options,question_number):
    #print(options)
    keyboard=[[telegram.InlineKeyboardButton(f"{options[i]}", callback_data=f'question {question_number}: {i}')] for i in range(len(options))]
    return telegram.InlineKeyboardMarkup(keyboard)

  def save_result(self,input_file):
    file=open(self.load_address, "w+")
    file.write(json.dumps(input_file))
    file.close()

  def load_result(self):
    file=open(self.load_address, "r")
    users=json.load(file)
    file.close()
    return users
  def question(self,update, context):
      if not update.callback_query is None:
        query = update.callback_query
        id=str(query.from_user.username)
      else:
        id=str(update.message.from_user.username)
     # print(id)
      if self.users[id]["question"]<self.questions.shape[0]:
        row=self.questions.iloc[self.users[id]["question"]]
        question=row["question"]
        options=row["options"]
        number_of_options=row["number_of_options"]
        question_type=row["type"]
        self.users[id]["question_shown"]=True
        if question_type=="mo":
          reply_markup = self.create_button(options,self.users[id]["question"])
          update.effective_chat.send_message(f"{question}",reply_markup=reply_markup)
        else:
          update.effective_chat.send_message(f"{question}")
      else:
        self.save_result(self.users)
        update.effective_chat.send_message(text=f'رشد و پیشرفت ما جز با همراهی شما میسر نمی باشد . ممنون از پاسخگویی و وقتی که در اختیار ما گذاشتید ')



  def handle_message(self,update, context):
      id=str(update.message.from_user.username)
      #print(id)
      
      if id not in self.users.keys():
        update.message.reply_text("شما شروع نکرده اید")
      else:
        if self.users[id]["question_shown"]==True:
          row=self.questions.iloc[self.users[id]["question"]]
          question=row["question"]
          options=row["options"]
          question_type=row["type"]
          number_of_options=row["number_of_options"]

          if question_type=="text":
            self.users[id]["question"]+=1
            self.users[id]["question_shown"]=False
            self.users[id]["answers"].append(str(update.message.text))
            update.message.reply_text("دریافت شد")
            self.question(update,context)
          else:
            update.message.reply_text("از طریق گزینه ها جواب دهید")
            
        else:
          update.message.reply_text("دوست عزیز شما به نظرسنجی ما پاسخ داده اید . چنانچه هرگونه سوال و یا پیشنهادی دارید میتوانید با کارشناسان ما ارتباط برقرار کنید . @rastad_support")

  def handle_button(self,update, context):
      query = update.callback_query
      id=str(query.from_user.username)
      query.answer()
      ans=str(query.data)
      if ans=="بپرس":
        query.delete_message()
        self.question(update,context)
      else:
        if self.users[id]["question_shown"]==True:
            row=self.questions.iloc[self.users[id]["question"]]
            self.users[id]["question"]+=1
            self.users[id]["question_shown"]=False
            self.users[id]["answers"].append(ans)
            query.edit_message_text(text=f"دریافت شد")
            self.question(update,context)
        else:
            query.edit_message_text(text=f"دوست عزیز شما به نظرسنجی ما پاسخ داده اید . چنانچه هرگونه سوال و یا پیشنهادی دارید میتوانید با کارشناسان ما ارتباط برقرار کنید . @rastad_support")

b=bot()

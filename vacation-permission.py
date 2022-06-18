import logging
import logging.handlers
from typing import ContextManager
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
from telethon import TelegramClient, events, sync
from datetime import date


home_dir = os.path.expanduser('~')
desktop_dir = os.path.join(home_dir, 'Desktop/permission telegram bot')
app = Flask(__name__)




Maneger , NewPermission,MonthButt , EndingMonth ,  EndMonthing  , StartingDay , EndMonth , StartDay ,EndDay , BeforeResult, ResultFinal , Permission ,Final = range(13)
One , Two , Three , Four , Five , Six , Seven , Eight , Nine , Ten , Eleven , Twelve , Therteen = range(13)
eOne , eTwo , eThree , eFour , eFive , eSix , eSeven , eEight , eNine , eTen , eEleven , eTwelve , eTherteen = range(13)
eeOne , eeTwo , eeThree , eeFour , eeFive , eeSix , eeSeven , eeEight , eeNine , eeTen , eeEleven , eeTwelve , eeTherteen = range(13)
no , yes , send = range(3)
eno , eyes , final= range(3)
refuse , ok = range(2)
Perno = range(1)
fuck1 , fuck2 = range(2)

def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['درخواست مرخصی جدید'], ['/start'],['/cancel']]

    update.message.reply_text(
        
        'سلام به بات درخواست مرخصی راستاد خوش اومدی '
        '\n\n'
        'حتما مثل گفته های بات پیش برو و هرجا که دیدی اشتباه کردی /cancel رو تایپ کن تا به حالت اول برگردی اگرم خواستی یک بار دیگه مرخصی ثبت کنی کافیه بزنی /start'
        '\n\n'
        ,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True
        ),
    )

    return NewPermission



def NewPerm(update: Update, context: CallbackContext,) -> int:

    user = update.message.from_user
    #logger.info("Run Bot with %s: %s", user.first_name, update.message.text)
    
    keyboard = [
        [
          InlineKeyboardButton("فروردین", callback_data=str(One)),
          InlineKeyboardButton("اردیبهشت", callback_data=str(Two)),
          InlineKeyboardButton("خرداد", callback_data=str(Three)),
        ],
        [
          InlineKeyboardButton("تیر", callback_data=str(Four)),
          InlineKeyboardButton("مرداد", callback_data=str(Five)),
          InlineKeyboardButton("شهریور", callback_data=str(Six)),
        ],[
          InlineKeyboardButton("مهر", callback_data=str(Seven)),
          InlineKeyboardButton("آبان", callback_data=str(Eight)),
          InlineKeyboardButton("آذر", callback_data=str(Nine)),
        ],[
          InlineKeyboardButton("دی", callback_data=str(Ten)),
          InlineKeyboardButton("بهمن", callback_data=str(Eleven)),
          InlineKeyboardButton("اسفند", callback_data=str(Twelve)),
        ],
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'ماه شروع مرخصیت رو انتخاب کن ' , reply_markup = reply_markup
        ),
    return MonthButt
  
def one(update: Update, context: CallbackContext) -> int:
 
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'1'
     )
  query.message.reply_text(
    "ماه انتخابی : فروردین"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
    )
  return EndMonth
def two(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
    savefile.write(
         f'{chat_id.username}'
         '\n'
         f'2'
     )
  query.message.reply_text(
    "ماه انتخابی : اردیبهشت"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
    )  
  return EndMonth
def three(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'3'
     )
  query.message.reply_text(
     "ماه انتخابی : خرداد"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
     , reply_markup = reply_markup
    )  
  return EndMonth
def four(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'4'
     )
  query.message.reply_text(
     "ماه انتخابی : تیر"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
     , reply_markup = reply_markup
    )  
  return EndMonth
def five(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'5'
     )
  query.message.reply_text(  
    "ماه انتخابی : مرداد"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
  )  
  return EndMonth
def six(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'6'
     )
  query.message.reply_text(
     "ماه انتخابی : شهریور"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
  )  
  return EndMonth
def seven(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'7'
     )
  query.message.reply_text(
    "ماه انتخابی : مهر"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
     , reply_markup = reply_markup
  ) 
  return EndMonth
def eight(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'8'
     )
  query.message.reply_text(
     "ماه انتخابی : آبان"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
  )
  return EndMonth
def nine(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'9'
     )
  query.message.reply_text(
     "ماه انتخابی : آذر"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
  )
  return EndMonth
def ten(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'10'
     )
  query.message.reply_text(
    "ماه انتخابی : دی"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
  )          
  return EndMonth
def eleven(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'11'
     )
  query.message.reply_text(
    "ماه انتخابی : بهمن"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
  ) 
  return EndMonth
def twelve(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(Therteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
     savefile.write(
         f'{chat_id.username}'
         '\n'
         f'12'
     )
  query.message.reply_text(
    "ماه انتخابی : اسفند"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    , reply_markup = reply_markup
  ) 
  return EndMonth  
def therteen(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  query.message.reply_text("ماه انتخابیتان ثبت شد  حالا لطفا ماهی که مرخصیتان به اتمام میرسد را انتخاب کنید") 
  return EndMonth 

def ending_month(update: Update, context: CallbackContext,) -> int:
   
    query = update.callback_query
    query.answer()
    
    
    keyboard = [
        [
          InlineKeyboardButton("فروردین", callback_data=str(eOne)),
          InlineKeyboardButton("اردیبهشت", callback_data=str(eTwo)),
          InlineKeyboardButton("خرداد", callback_data=str(eThree)),
        ],
        [
          InlineKeyboardButton("تیر", callback_data=str(eFour)),
          InlineKeyboardButton("مرداد", callback_data=str(eFive)),
          InlineKeyboardButton("شهریور", callback_data=str(eSix)),
        ],[
          InlineKeyboardButton("مهر", callback_data=str(eSeven)),
          InlineKeyboardButton("آبان", callback_data=str(eEight)),
          InlineKeyboardButton("آذر", callback_data=str(eNine)),
        ],[
          InlineKeyboardButton("دی", callback_data=str(eTen)),
          InlineKeyboardButton("بهمن", callback_data=str(eEleven)),
          InlineKeyboardButton("اسفند", callback_data=str(eTwelve)),
        ],
        
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.message.reply_text(
        'ماه پایان مرخصیت رو انتخاب کن ' , reply_markup = reply_markup
        ),
    return EndingMonth
def eone(update: Update, context: CallbackContext) -> int:
 
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'1'
     )
  query.message.reply_text(
    "ماه انتخابی : فروردین"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
    )
  return EndMonthing 
def etwo(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'2'
     )
  query.message.reply_text(
    "ماه انتخابی : اردیبهشت"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
    )  
  return EndMonthing 
def ethree(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'3'
     )
  query.message.reply_text(
     "ماه انتخابی : خرداد"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
    )  
  return EndMonthing 
def efour(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'4'
     )
  query.message.reply_text(
     "ماه انتخابی : تیر"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
    )  
  return EndMonthing 
def efive(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'5'
     )
  query.message.reply_text(  
    "ماه انتخابی : مرداد"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  )  
  return EndMonthing 
def esix(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'6'
     )
  query.message.reply_text(
     "ماه انتخابی : شهریور"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  )  
  return EndMonthing 
def eseven(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'7'
     )
  query.message.reply_text(
    "ماه انتخابی : مهر"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  ) 
  return EndMonthing 
def eeight(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'8'
     )
  query.message.reply_text(
     "ماه انتخابی : آبان"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  )
  return EndMonthing 
def enine(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'9'
     )
  query.message.reply_text(
     "ماه انتخابی : آذر"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  )
  return EndMonthing 
def eten(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'10'
     )
  query.message.reply_text(
    "ماه انتخابی : دی"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  )          
  return EndMonthing 
def eeleven(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'11'
     )
  query.message.reply_text(
    "ماه انتخابی : بهمن"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  ) 
  return EndMonthing 
def etwelve(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  keyboard = [
        [
          InlineKeyboardButton("فرستادن ماه ", callback_data=str(eTherteen)),
        ],
       ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  with open('./readme.txt', 'a+', encoding="utf-8" ) as savefile:
     savefile.write(
         '\n'
         f'12'
     )
  query.message.reply_text(
    "ماه انتخابی : اسفند"
    "\n\n"
    "درصورت اوکی بودن روی دکمه ی ارسال ماه کلیک کنید"
    ,reply_markup=reply_markup
  ) 
  return EndMonthing  
def etherteen(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_user
  return StartingDay

def starting_day(update: Update, context: CallbackContext,) -> int:
   
    query = update.callback_query
    query.answer()
    chat_id=update.effective_user
    query.message.reply_text("ممنون ، حالا روز انتخابیت برای شروع مرخصی رو انتخاب کن") 
    return StartDay

def starting_day2(update: Update, context: CallbackContext,) -> int:
   
    with open('./readme.txt', 'a', encoding="utf-8" ) as savefile:
     savefile.write( 
         '\n'
         f'{update.message.text}'
     )
     update.message.reply_text(
       f"روز انتخابی : {update.message.text}"
       "\n\n"
       "حالا روزی که مرخصیت به پایان میرسه رو هم برام تایپ کن"
     )
    return EndDay

def Before_Result(update: Update, context: CallbackContext) -> int:
  
    user = update.message.from_user
    with open('./readme.txt', 'a', encoding="utf-8" ) as savefile:
     savefile.write( 
         '\n'
         f'{update.message.text}'
     )
    update.message.reply_text(
        f'تاریخ پایان : {update.message.text} ام'
        '\n\n'
        'مرسی ازت  اینم از درخواستت .👇' 
    )
    with open('./readme.txt', encoding='utf-8') as f:
     lines = f.readlines()
    startmonth = lines[1].replace("\n","")
    endmonth = lines[2].replace("\n" , "")
    enddate = lines[4].replace("\n" , "")
    startdate = lines[3].replace("\n" , "")
    
    
    chat_id=update.effective_chat.id
    if chat_id == 382215836:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Amir"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
         'درخواست مرخصی کارمند : امیر محمد احمدی '
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
        f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
          'درخواست مرخصی کارمند : امیر محمد احمدی '
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        
        )
    if chat_id == 380855812:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Moein"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
          'درخواست مرخصی کارمند : معین یکه زارع'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
          'درخواست مرخصی کارمند : معین یکه زارع'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        
        )   
    if chat_id == 92269219:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Mostafa"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
          'درخواست مرخصی کارمند : مصطفی میرزایی'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
         f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی کارمند : مصطفی میرزایی'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        )   
    
    if chat_id == 75674253:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Mahsa"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
          'درخواست مرخصی کارمند : مهسا ملکی '
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی کارمند : مهسا ملکی '
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
       
        )   
    if chat_id == 224411560:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Saba"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
          'درخواست مرخصی کارمند: صبا سزشکی'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
         f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی کارمند: صبا سزشکی'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
           f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        
        )   
    
    if chat_id == 104789594:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Salah"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
         'درخواست مرخصی کارمند : صلاح الدین رامتین'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
         f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی کارمند : صلاح الدین رامتین'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        
        )   
    if chat_id == 1202145410:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Mohsen"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
         'درخواست مرخصی کارمند : محسن احدی نژاد'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : { a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی کارمند : محسن احدی نژاد'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n'
        ':)))) ردش کن یکم عشق کنیم'
        )   
    if chat_id == 101838225:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Shahla"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
          'درخواست مرخصی کارمند : شهلا محمدی'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
         f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : { a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی کارمند : شهلا محمدی'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n'
        ':)))) ردش کن یکم عشق کنیم'
        ) 
    if chat_id == 419120272:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Pouyan"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
          'درخواست مرخصی کارمند : پویان پرتو'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
         f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی کارمند : پویان پرتو'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
          f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n'
        ':)))) ردش کن یکم عشق کنیم'
        ) 
    if chat_id == 266176776:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["AliS"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
          'درخواست مرخصی کارمند : علی راهنما'
        '\n\n'
        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
         f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : { a-x}"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
          'درخواست مرخصی کارمند : علی راهنما'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
           f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a-x}"
        '\n'
        ':)))) ردش کن یکم عشق کنیم'
        ) 
    if chat_id == 87784611:
      with open("./json_data.json", "r") as jsonfile:
       data = json.load(jsonfile)
       a = data["Ebrahimi"]
       f_date = date(2021, int(startmonth), int(startdate))
       l_date = date(2021, int(endmonth), int(enddate))
       if int(startmonth) == int(endmonth): 
        days = l_date - f_date 
        x = days.days
       else:
        days = l_date - f_date
        x = days.days
        x = x - 1
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text(
         'درخواست مرخصی مدیر : بهروز ابراهیمی'
        '\n\n'

        '⏰'
        f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
        '\n\n'
        '⏰'
         f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n\n'
        f"تعداد روزهای باقی مانده برای مرخصی : { a-x }"
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست مرخصی مدیر : بهروز ابراهیمی'
         '\n'
         '⏰'
         f' تاریخ شروع درخواست 👈 {startdate} / {startmonth}'
         '\n'
         '⏰'
           f'تاریخ پایان درخواست 👈 {enddate} / {endmonth}'
        '\n'
         f"تعداد روزهای باقی مانده برای مرخصی : {a - x}"
        '\n'
       
        ) 

    return ResultFinal

def button( update: Update,  context: CallbackContext) -> int:
        query = update.callback_query
        query.answer()
        chat_id=update.effective_chat.id
        query.edit_message_text(text=f"ممنون از درخواستتان")
        if chat_id == 382215836:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Amir"] = data["Amir"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()

        if chat_id == 266176776:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["AliS"] = data["AliS"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()   

        if chat_id == 380855812:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           days = int(enddate) - int(startdate)
           data["Moein"] = data["Moein"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines() 
        
        if chat_id == 92269219:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Mostafa"] = data["Mostafa"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines() 

        if chat_id == 75674253:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Mahsa"] = data["Mahsa"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()    
        
        if chat_id == 224411560:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Saba"] = data["Saba"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()    

        if chat_id == 104789594:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Salah"] = data["Salah"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines() 

        if chat_id == 1202145410:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Mohsen"] = data["Mohsen"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines() 

        if chat_id == 101838225:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Shahla"] = data["Shahla"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()  

        if chat_id == 419120272:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Pouyan"] = data["Pouyan"] - x
           json.dump(data , jsonfile)
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines() 

        

        if chat_id == 87784611:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
          with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
          with open("./json_data.json", "w") as jsonfile:
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Ebrahimi"] = data["Ebrahimi"] - x
           json.dump(data , jsonfile)
        keyboard5 = [
          [
        InlineKeyboardButton("اتمام درخواست", callback_data = str(final)  ),
                   ]]
        reply_markup3 = InlineKeyboardMarkup(keyboard5)
        query.edit_message_text(text=f"درخواستتان برای مدیر ارسال شد ، لطفا منتظر پاسخشان از طریق من باشید . و برای ذخیره اطلاعات درخواستتان و همچنین خاموش شدن بات دکمه ی اتمام درخواست را بزنید",reply_markup = reply_markup3)

        return Permission

def peryes(update: Update,context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  query.edit_message_text(text = "برای شروع دوباره از بات /start  را بزنید")
  with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
  
  reply_keyboard = [['/accept'],['/refuse']]
  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
  bot_message =lines[0] + '\n' + lines[1] + '\n' + lines[2] + '\n' + lines[3] + '\n'
  context.bot.send_message(chat_id=-1001291669925, text=bot_message , reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True) )
  return ConversationHandler.END

def perno(update: Update, context: CallbackContext) -> int:
  with open('./readme.txt', encoding="utf-8") as f:
    lines = f.readlines()
  x = lines[0].replace('\n', '')
  if x == "Amirm_1376":
    update.message.reply_text("پیام تایید مرخصی برای امیر ارسال شد" )
    context.bot.send_message(chat_id=382215836, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "Mn_ahadi_Nejad":
    update.message.reply_text("پیام تایید مرخصی برای محسن ارسال شد")
    context.bot.send_message(chat_id=1202145410, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "Sha412":
    update.message.reply_text("پیام تایید مرخصی برای شهلا ارسال شد")
    context.bot.send_message(chat_id=101838225, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "Behrooz_ebrahimi":
    update.message.reply_text("پیام تایید مرخصی برای بهروز ارسال شد")
    context.bot.send_message(chat_id=87784611, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "AliSRnm":
    update.message.reply_text("پیام تایید مرخصی برای علی راهنما ارسال شد")
    context.bot.send_message(chat_id=266176776, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "SlhDono":
    update.message.reply_text("پیام تایید مرخصی برای صلاح ارسال شد ")
    context.bot.send_message(chat_id=104789594, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "pooyanp2":
    update.message.reply_text("پیام تایید مرخصی برای پویان ارسال شد")
    context.bot.send_message(chat_id=419120272, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "mostafa_mirzaee_9":
    update.message.reply_text("پیام تایید مرخصی برای مصطفی ارسال شد")
    context.bot.send_message(chat_id=92269219, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "Sabask":
    update.message.reply_text("پیام تایید مرخصی برای صبا ارسال شد")
    context.bot.send_message(chat_id=224411560, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "mahsa_mls":
    update.message.reply_text("پیام تایید مرخصی برای مهسا ارسال شد")
    context.bot.send_message(chat_id=75674253, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  if x == "moein_yz":
    update.message.reply_text("پیام تایید مرخصی برای معین ارسال شد")
    context.bot.send_message(chat_id=380855812, text="✅درخواست شما برای مرخصی از طرف مدیریت مورد قبول واقع شد" )
  return ConversationHandler.END

def man(update: Update, context: CallbackContext) -> int:
  with open('./readme.txt', encoding="utf-8") as f:
    lines = f.readlines()
  x = lines[0].replace('\n', '')
  if x == "Amirm_1376":
      update.message.reply_text("پیام رد مرخصی برای امیر ارسال شد" )
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Amir"] = data["Amir"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id=382215836, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️")
  if x == "Mn_ahadi_Nejad":
      update.message.reply_text("پیام رد مرخصی برای محسن ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Mohsen"] = data["Mohsen"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id=1202145410, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️")
  if x == "moein_yz":
      update.message.reply_text("پیام رد مرخصی برای معین ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Moein"] = data["Moein"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id=380855812, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️")
  if x == "Sha412":
      update.message.reply_text("پیام رد مرخصی برای شهلا ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Shahla"] = data["Shahla"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id=101838225, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  if x == "Behrooz_ebrahimi":
      update.message.reply_text("پیام رد مرخصی برای بهروز ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Ebrahimi"] = data["Ebrahimi"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id= 87784611, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  if x == "AliSRnm":
      update.message.reply_text("پیام رد مرخصی برای علی راهنما ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["AliS"] = data["AliS"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id= 266176776, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  if x == "SlhDono":
      update.message.reply_text("پیام رد مرخصی برای صلاح ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Salah"] = data["Salah"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id= 104789594, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  if x == "pooyanp2":
      update.message.reply_text("پیام رد مرخصی برای پویان ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Pouyan"] = data["Pouyan"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id= 419120272, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  if x == "mostafa_mirzaee_9":
      update.message.reply_text("پیام رد مرخصی برای مصطفی ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Mostafa"] = data["Mostafa"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id= 92269219, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  if x == "Sabask":
      update.message.reply_text("پیام رد مرخصی برای صبا ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Saba"] = data["Saba"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id= 224411560, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  if x == "mahsa_mls":
      update.message.reply_text("پیام رد مرخصی برای مهسا ارسال شد")
      with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           enddate = lines[4].replace("\n" , "")
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
      with open("./json_data.json", "r") as jsonfile:
           data = json.load(jsonfile)
      with open("./json_data.json", "w") as jsonfile:
           f_date = date(2021, int(startmonth), int(startdate))
           l_date = date(2021, int(endmonth), int(enddate))
           if int(startmonth) == int(endmonth): 
            days = l_date - f_date 
            x = days.days
           else:
            days = l_date - f_date
            x = days.days
            x = x - 1
           data["Mahsa"] = data["Mahsa"] + x
           json.dump(data , jsonfile)
      context.bot.send_message(chat_id= 75674253, text ="⛔️درخواست شما برای مرخصی از طرف مدیریت مورد قبول وافع نشد ⛔️" )
  return ConversationHandler.END
  



def button2(update: Update, context: CallbackContext) -> int:
  query = update.callback_query
  query.answer()
  chat_id=update.effective_chat.id
  query.edit_message_text(text =
             'برای استفاده دوباره از بات ابتدا /cancel  را تایپ کرده و بفرستید و سپس /start  را بزنید'           
        )
  return Permission




def cancel(update: Update, context: CallbackContext) -> int:
    #logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'برای شروع دوباره /start  زا تایپ کنید ', reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END
    
@app.route('/', methods=['GET', 'POST'])
def main() -> None:
    updater = Updater("")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[
        CommandHandler('start', start),
        CommandHandler('accept', perno),
        CommandHandler('refuse', man),
        ],
        states={
            NewPermission: [MessageHandler(Filters.regex('^(درخواست مرخصی جدید)$'), NewPerm)],
            MonthButt: [
              CallbackQueryHandler(one, pattern='^' + str(One) + '$'),
              CallbackQueryHandler(two, pattern='^' + str(Two) + '$'),
              CallbackQueryHandler(three, pattern='^' + str(Three) + '$'),
              CallbackQueryHandler(four, pattern='^' + str(Four) + '$'),
              CallbackQueryHandler(five, pattern='^' + str(Five) + '$'),
              CallbackQueryHandler(six, pattern='^' + str(Six) + '$'),
              CallbackQueryHandler(seven, pattern='^' + str(Seven) + '$'),
              CallbackQueryHandler(eight, pattern='^' + str(Eight) + '$'),
              CallbackQueryHandler(nine, pattern='^' + str(Nine) + '$'),
              CallbackQueryHandler(ten, pattern='^' + str(Ten) + '$'),
              CallbackQueryHandler(eleven, pattern='^' + str(Eleven) + '$'),
              CallbackQueryHandler(twelve, pattern='^' + str(Twelve) + '$'),
              ],
            EndMonth: [
              CallbackQueryHandler(ending_month, pattern='^' + str(Therteen) + '$'),
            ],
            EndingMonth:[
              CallbackQueryHandler(eone, pattern='^' + str(eOne) + '$'),
              CallbackQueryHandler(etwo, pattern='^' + str(eTwo) + '$'),
              CallbackQueryHandler(ethree, pattern='^' + str(eThree) + '$'),
              CallbackQueryHandler(efour, pattern='^' + str(eFour) + '$'),
              CallbackQueryHandler(efive, pattern='^' + str(eFive) + '$'),
              CallbackQueryHandler(esix, pattern='^' + str(eSix) + '$'),
              CallbackQueryHandler(eseven, pattern='^' + str(eSeven) + '$'),
              CallbackQueryHandler(eeight, pattern='^' + str(eEight) + '$'),
              CallbackQueryHandler(enine, pattern='^' + str(eNine) + '$'),
              CallbackQueryHandler(eten, pattern='^' + str(eTen) + '$'),
              CallbackQueryHandler(eeleven, pattern='^' + str(eEleven) + '$'),
              CallbackQueryHandler(etwelve, pattern='^' + str(eTwelve) + '$'),
            ],
            EndMonthing:[
              CallbackQueryHandler(starting_day, pattern='^' + str(eTherteen) + '$'),
            ],
            
            StartDay:[MessageHandler(Filters.text & ~Filters.command, starting_day2)],
            EndDay:[MessageHandler(Filters.text & ~Filters.command, Before_Result)],
            ResultFinal: [
              CallbackQueryHandler(button, pattern='^' + str(yes) + '$'),
              CallbackQueryHandler(button2, pattern='^' + str(no) + '$'),
            ],
            Permission:[
              CallbackQueryHandler(peryes, pattern='^' + str(final) + '$'),
            ],
        },
        
        fallbacks=[CommandHandler('cancel', cancel),],
        
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    
    updater.idle()
    

if __name__ == '__main__':
    main()
    app.run(debug=True)
    


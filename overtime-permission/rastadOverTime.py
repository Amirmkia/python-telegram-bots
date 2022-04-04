from argparse import ONE_OR_MORE
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


Maneger , NewPermission,MonthButt , EndingMonth ,  EndMonthing  , StartingDay , EndMonth , StartDay ,EndDay , Questionone , Questiontwo ,   BeforeResult, ResultFinal , Permission ,Final = range(15)
One , Two , Three , Four , Five , Six , Seven , Eight , Nine , Ten , Eleven , Twelve , Therteen = range(13)
eOne , eTwo , eThree , eFour , eFive , eSix , eSeven , eEight , eNine , eTen , eEleven , eTwelve , eTherteen = range(13)
eeOne , eeTwo , eeThree , eeFour , eeFive , eeSix , eeSeven , eeEight , eeNine , eeTen , eeEleven , eeTwelve , eeTherteen = range(13)
no , yes , send = range(3)
eno , eyes , final= range(3)
refuse , ok = range(2)
Perno = range(1)
fuck1 , fuck2 = range(2)
marketting , tahlil , fanni = range(3)
newperm , cancelit = range(2)
startagain = range(1)
def start(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [
          InlineKeyboardButton("درخواست مرخصی جدید", callback_data=str(newperm)),
          InlineKeyboardButton("لغو", callback_data=str(cancelit)),
        ]
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'سلام به بات درخواست اضافه کاری راستاد خوش اومدی  '
        '\n\n'
        'حتما مثل گفته های بات پیش برو و هرجا که دیدی اشتباه کردی /cancel رو تایپ کن تا به حالت اول برگردی اگرم خواستی یک بار دیگه اضافه کاری ثبت کنی کافیه بزنی /start'
        '\n\n'
        , reply_markup = reply_markup
    )

    return NewPermission

def NewPerm(update: Update, context: CallbackContext,) -> int:  
    query = update.callback_query
    query.answer()  
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
    query.message.reply_text(
        'ماه شروع اضافه کاریت رو انتخاب کن ' , reply_markup = reply_markup
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
         f'فروردین'
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
         f'اردیبهشت'
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
         f'خرداد'
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
         f'تیر'
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
         f'مرداد'
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
         f'شهریور'
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
         f'مهر'
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
         f'آبان'
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
         f'آذر'
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
         f'دی'
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
         f'بهمن'
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
         f'اسفند'
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
  query.message.reply_text(
    "ماه انتخابیتان ثبت شد "
  ) 
  return StartingDay

def starting_day(update: Update, context: CallbackContext,) -> int:
   
    query = update.callback_query
    query.answer()
    chat_id=update.effective_user
    if query.data == "0":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'فروردین'
        )
    if query.data == "1":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'اردیبهشت'
        )
    if query.data == "2":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'خرداد'
        )
    if query.data == "3":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'تیر'
        )
    if query.data == "4":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'مرداد'
        )
    if query.data == "5":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'شهریور'
        )
    if query.data == "6":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'مهر'
        )
    if query.data == "7":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'آبان'
        )
    if query.data == "8":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'آذر'
        )
    if query.data == "9":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'دی'
        )
    if query.data == "10":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'بهمن'
        )
    if query.data == "11":
        with open('./readme.txt', 'w', encoding="utf-8" ) as savefile:
           savefile.write(
             f'{chat_id.username}'
             '\n'
             f'اسفند'
        )
    query.message.reply_text(
      "حالا لطفا تاریخ روزی که میخواهید اضافه کاری کنید را وارد کنید"
      "\n\n"
      "برای مثال : میخواهید 11 آبان اضافه کاری وایسید بنویسید : 11"
      ) 
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
       "حالا ساعاتی که میخواهید اضافه بمانید را ثبت کنید "
       "\n\n"
       "مثلا بنویسید : از ساعت 17 تا 20"
     )
    # return EndDay
    return Questionone
def questionone(update: Update, context: CallbackContext):
    with open('./readme.txt', 'a', encoding="utf-8" ) as savefile:
     savefile.write( 
         '\n'
         f'{update.message.text}'
     )
    update.message.reply_text(
        f'ساعاتی که ثبت کردید : {update.message.text}'
        '\n\n'
        'لطفا در پیامی کوتاه توضیح دهید که چه فعالیتی در این ساعات انجام خواهید داد ' 
    )
    return Questiontwo
def questiontwo(update: Update, context: CallbackContext):
    keyboard = [
        [
          InlineKeyboardButton("واحد مارکتینگ", callback_data=str(marketting)),
          InlineKeyboardButton("واحد تحلیل بازار", callback_data=str(tahlil)),
          InlineKeyboardButton("واحد فنی", callback_data=str(fanni)),
        ],
       ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open('./readme.txt', 'a', encoding="utf-8" ) as savefile:
     savefile.write( 
         '\n'
         f'{update.message.text}'
     )
    update.message.reply_text(
        f'ممنون'
        '\n\n'
        'لطفا دپارتمان خود را برایمان ارسال کنید' 
        , reply_markup = reply_markup
    )
    return EndDay

def Before_Result(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    chat_id=update.effective_user
    if query.data == "0":
      x = "واحد مارکتینگ"
    if query.data == "1":
      x = "واحد تحلیل"
    if query.data == "2":
      x = "واحد فنی"
    with open('./readme.txt', 'a', encoding="utf-8" ) as savefile:
     savefile.write( 
         '\n'
         f'{x}'
     )
    query.message.reply_text(
        f'دپارتمانی که انتخاب کردید: {x}'
        '\n\n'
        'مرسی ازت  اینم از درخواستت .👇' 
    )
    with open('./readme.txt', encoding='utf-8') as f:
     lines = f.readlines()
    startmonth = lines[1].replace("\n","")
    endmonth = lines[2].replace("\n" , "")
    startdate = lines[3].replace("\n" , "")
    questionone = lines[4].replace("\n" , "")
    questiontwo = lines[5].replace("\n", "")
    
    chat_id=update.effective_chat.id
    if chat_id == 382215836:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
         'درخواست اضافه کاری کارمند : امیر محمد احمدی '
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
          'درخواست اضافه کاری کارمند : امیر محمد احمدی '
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        )
    if chat_id == 380855812:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
          'درخواست اضافه کاری کارمند : معین یکه زارع'
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
          'درخواست اضافه کاری کارمند : معین یکه زارع'
          '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        )   
    if chat_id == 92269219:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
          'درخواست اضافه کاری کارمند : مصطفی میرزایی'
         '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست اضافه کاری کارمند : مصطفی میرزایی'
         '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        )   
    
    if chat_id == 75674253:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
          'درخواست اضافه کاری کارمند : مهسا ملکی '
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست اضافه کاری کارمند : مهسا ملکی '
         '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
       
        )   
    if chat_id == 224411560:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
          'درخواست اضافه کاری کارمند: صبا سزشکی'
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست اضافه کاری کارمند: صبا سزشکی'
         '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        )   
    
    if chat_id == 104789594:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
         'درخواست اضافه کاری کارمند : صلاح الدین رامتین'
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست اضافه کاری کارمند : صلاح الدین رامتین'
         '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        )   
    if chat_id == 1202145410:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
         'درخواست اضافه کاری کارمند : محسن احدی نژاد'
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
           'درخواست اضافه کاری کارمند : محسن احدی نژاد'
         '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        )   
    if chat_id == 266176776:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
          'درخواست اضافه کاری کارمند : علی راهنما'
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
          'درخواست اضافه کاری کارمند : علی راهنما'
         '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        ) 
    if chat_id == 87784611:
       keyboard = [
        [
          InlineKeyboardButton("⛔️لغو", callback_data=str(no)),
          InlineKeyboardButton("✅ ارسال", callback_data=str(yes)),
        ],
        ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       query.message.reply_text(
         'درخواست اضافه کاری کارمند : بهروز ابراهیمی '
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
        '❗️❗️❗️'
        'اگه درسته که دکمه ی ارسال به مدیر رو بزن و منتظر باش تا مدیر جواب درخواستت رو  بهت بگه و اگه اوکی نیستی دکمه ی لغو درخواست رو بزن تا درخواستت رو پاک کنم '
        '❗️❗️❗️',reply_markup=reply_markup
        )
       with open('./finall.txt', 'w', encoding="utf-8" ) as savefile:
          savefile.write(
          'درخواست اضافه کاری کارمند : بهروز ابراهیمی '
        '\n\n'
        '⏰'
        f' تاریخ درخواست 👈 {endmonth} / {startmonth}'
        '\n\n'
        '⏰'
        f'ساعات درخواست اضافه کاری 👈{startdate}'
        '\n\n'
        f'خلاصه فعالیت : 👈{questionone}'
        '\n\n'
        f'دپارتمان : 👈{questiontwo}'
        '\n\n'
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
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()

        if chat_id == 266176776:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 380855812:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 92269219:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 75674253:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 224411560:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 104789594:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 1202145410:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 101838225:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 419120272:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
        if chat_id == 87784611:
          with open('./readme.txt', encoding='utf-8') as f:
           lines = f.readlines()
           startdate = lines[3].replace("\n" , "")
           startmonth = lines[1].replace("\n","")
           endmonth = lines[2].replace("\n" , "")
          with open('./finall.txt', encoding="utf-8") as f:
           lines = f.readlines()
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
  bot_message =lines[0] + '\n' + lines[1] + lines[2] + lines[3] + lines[4] + lines[5] + lines[6] + lines[7] + lines[8]
  context.bot.send_message(chat_id=-1001291669925, text=bot_message , reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True) )
  return ConversationHandler.END

def perno(update: Update, context: CallbackContext) -> int:
  with open('./readme.txt', encoding="utf-8") as f:
    lines = f.readlines()
  x = lines[0].replace('\n', '')
  if x == "Amirm_1376":
    update.message.reply_text("پیام تایید اضافه کاری برای امیر ارسال شد", reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=382215836, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "Mn_ahadi_Nejad":
    update.message.reply_text("پیام تایید اضافه کاری برای محسن ارسال شد" , reply_markup = ReplyKeyboardRemove())
    context.bot.send_message(chat_id=1202145410, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "Sha412":
    update.message.reply_text("پیام تایید اضافه کاری برای شهلا ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=101838225, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "Behrooz_ebrahimi":
    update.message.reply_text("پیام تایید اضافه کاری برای بهروز ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=87784611, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "AliSRnm":
    update.message.reply_text("پیام تایید اضافه کاری برای علی راهنما ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=266176776, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "SlhDono":
    update.message.reply_text("پیام تایید اضافه کاری برای صلاح ارسال شد " , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=104789594, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "pooyanp2":
    update.message.reply_text("پیام تایید اضافه کاری برای پویان ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=419120272, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "mostafa_mirzaee_9":
    update.message.reply_text("پیام تایید اضافه کاری برای مصطفی ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=92269219, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "Sabask":
    update.message.reply_text("پیام تایید اضافه کاری برای صبا ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=224411560, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "mahsa_mls":
    update.message.reply_text("پیام تایید اضافه کاری برای مهسا ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=75674253, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  if x == "moein_yz":
    update.message.reply_text("پیام تایید اضافه کاری برای معین ارسال شد" , reply_markup = ReplyKeyboardRemove() )
    context.bot.send_message(chat_id=380855812, text="✅درخواست شما برای اضافه کاری از طرف مدیریت قبول شد" )
  return ConversationHandler.END

def man(update: Update, context: CallbackContext) -> int:
  with open('./readme.txt', encoding="utf-8") as f:
    lines = f.readlines()
  x = lines[0].replace('\n', '')
  if x == "Amirm_1376":
      update.message.reply_text("پیام رد اضافه کاری برای امیر ارسال شد" , reply_markup = ReplyKeyboardRemove() )
      context.bot.send_message(chat_id=382215836, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️")
  if x == "Mn_ahadi_Nejad":
      update.message.reply_text("پیام رد اضافه کاری برای محسن ارسال شد" , reply_markup = ReplyKeyboardRemove() )
      context.bot.send_message(chat_id=1202145410, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️")
  if x == "moein_yz":
      update.message.reply_text("پیام رد اضافه کاری برای معین ارسال شد" , reply_markup = ReplyKeyboardRemove() )
      context.bot.send_message(chat_id=380855812, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️")
  if x == "Sha412":
      update.message.reply_text("پیام رد اضافه کاری برای شهلا ارسال شد" , reply_markup = ReplyKeyboardRemove() )
      context.bot.send_message(chat_id=101838225, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
  if x == "Behrooz_ebrahimi":
      update.message.reply_text("پیام رد اضافه کاری برای ابراهیمی ارسال شد" , reply_markup = ReplyKeyboardRemove() )
      context.bot.send_message(chat_id= 87784611, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
  if x == "AliSRnm":
      update.message.reply_text("پیام رد اضافه کاری برای علی راهنما ارسال شد" , reply_markup = ReplyKeyboardRemove())
      context.bot.send_message(chat_id= 266176776, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
  if x == "SlhDono":
      update.message.reply_text("پیام رد اضافه کاری برای صلاح ارسال شد" , reply_markup = ReplyKeyboardRemove())
      context.bot.send_message(chat_id= 104789594, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
  if x == "pooyanp2":
      update.message.reply_text("پیام رد اضافه کاری برای پویان ارسال شد" , reply_markup = ReplyKeyboardRemove())
      context.bot.send_message(chat_id= 419120272, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
  if x == "mostafa_mirzaee_9":
      update.message.reply_text("پیام رد اضافه کاری برای مصطفی ارسال شد" , reply_markup = ReplyKeyboardRemove())
      context.bot.send_message(chat_id= 92269219, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
  if x == "Sabask":
      update.message.reply_text("پیام رد اضافه کاری برای صبا ارسال شد" , reply_markup = ReplyKeyboardRemove())
      context.bot.send_message(chat_id= 224411560, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
  if x == "mahsa_mls":
      update.message.reply_text("پیام رد اضافه کاری برای مهسا ارسال شد" , reply_markup = ReplyKeyboardRemove())
      context.bot.send_message(chat_id= 75674253, text ="⛔️درخواست شما برای اضافه کاری از طرف مدیریت قبول نشد ⛔️" )
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
    query = update.callback_query
    query.answer()
    query.message.reply_text(
        'برای شروع دوباره /start  را تایپ کنید', reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END
def cancelit(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'برای شروع دوباره /start  را تایپ کنید', reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
@app.route('/', methods=['GET', 'POST'])
def main() -> None:
    updater = Updater("5051097802:AAFtATuJkP-29Hn1Y3ysI_Sis2l6s4CkNzQ")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[
        CommandHandler('start', start),
        CommandHandler('accept', perno),
        CommandHandler('refuse', man),
        ],
        
        states={
            NewPermission: [
                CallbackQueryHandler(NewPerm, pattern='^' + str(newperm) + '$'),
                CallbackQueryHandler(cancel, pattern='^' + str(cancelit) + '$'),
              ],
            MonthButt: [
              CallbackQueryHandler(starting_day, pattern='^' + str(One) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Two) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Three) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Four) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Five) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Six) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Seven) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Eight) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Nine) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Ten) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Eleven) + '$'),
              CallbackQueryHandler(starting_day, pattern='^' + str(Twelve) + '$'),
              ],
            
            EndMonth:[
              CallbackQueryHandler(starting_day, pattern='^' + str(Therteen) + '$'),
            ],
            
            StartDay:[MessageHandler(Filters.text & ~Filters.command, starting_day2)],
            Questionone : [MessageHandler(Filters.text & ~Filters.command, questionone)],
            Questiontwo : [MessageHandler(Filters.text & ~Filters.command, questiontwo)],
            EndDay:[
               CallbackQueryHandler(Before_Result, pattern='^' + str(marketting) + '$'),
               CallbackQueryHandler(Before_Result, pattern='^' + str(tahlil) + '$'),
               CallbackQueryHandler(Before_Result, pattern='^' + str(fanni) + '$'),
            ],
            ResultFinal: [
              CallbackQueryHandler(button, pattern='^' + str(yes) + '$'),
              CallbackQueryHandler(button2, pattern='^' + str(no) + '$'),
            ],
            Permission:[
              CallbackQueryHandler(peryes, pattern='^' + str(final) + '$'),
            ],
        },
        
        fallbacks=[CommandHandler('cancel', cancelit),],
        
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    app.run(debug=True)
    

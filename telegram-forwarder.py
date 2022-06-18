from telethon import TelegramClient, events

CHANNEL = "https://t.me/coin_listing"
api_id = ""
api_hash = ""

client = TelegramClient('amirforwarder', api_id, api_hash)

@client.on(events.NewMessage(chats = "https://t.me/coin_listing"))
async def my_event_handler(event):
    if event:
        await client.forward_messages(
        -1001458955463,  
        event.message 
         ) 
client.start()
client.run_until_disconnected()

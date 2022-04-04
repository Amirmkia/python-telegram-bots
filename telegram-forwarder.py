from telethon import TelegramClient, events

CHANNEL = "https://t.me/coin_listing"
api_id = "6507128"
api_hash = "3e7dea0acaef86a05fa54511a0f4f9c6"

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
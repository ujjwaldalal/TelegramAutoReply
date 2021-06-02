import time
from telethon import TelegramClient, events

# this is secret, do not share with anyone
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

phone = 'PHONE_NUMBER_IN_INTERNATIONAL_FORMAT'
password = 'YOUR_PASSWORD'  #use this if you have two factor authentication turned on for your account
session_file = '/path/to/session/file' #this is where your session data will persist. You can name the file anything you want.

message = 'This is autoreply message' #message to be sent in autoreply

if __name__ == '__main__':
    #Create the client
    # use sequential_updates=True to respond to messages one at a time
    client  = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)  

    @client.on(events.NewMessage(incoming=True)) #handle only incoming messages
    async def handle_new_message(event):
        if event.is_private: #only reply to private chats
            from_ = await event.client.get_entity(event.from_id)
            print(from_)
            print(time.asctime(), '-',  event.message)
            time.sleep(1)
            await event.respond(message)

    
    # Function to get all the open/current dialogs
    def setup():
        users = set()
        for dialog in client.iter_dialogs():
            if dialog.is_user:
                print(dialog)
                users.add(dialog.id)  
    
    
    print(time.asctime(), '-', 'Auto-replying turned on for you...')
    client.start(phone) # start client istance
    setup()
    client.run_until_disconnected() #run auto reply until disconnected 
    print(time.asctime(), '-', 'Stopped Auto-reply')

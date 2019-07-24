from telethon import TelegramClient, sync, events
from core import *

#chat_id = "MaryBakhtina"
chat_id = "katyn_katun"
play_list_name = "test"
min_message = 0

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=(chat_id)))
async def normal_handler(event):
    user_mess=event.message.to_dict()['message']
    api_play_music = PlayMusic()
    set_songs = set()
    track_id = Messages.get_track_id(user_mess)
    set_songs.add(track_id)
    
    api_play_music.add_setsong_to_play_list(play_list_name, set_songs)
    f.write(user_mess+"\n\n")

    f.flush()

client.start()

f=open('messages_from_chat', 'a') 

client.run_until_disconnected()
f.close()
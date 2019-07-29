from telethon import TelegramClient, sync, events
from core import *

chat_id = "MaryBakhtina"
#chat_id = "katyn_katun"
play_list_name = "Telegram music"
min_message = 0

client = TelegramClient('session_name', api_id, api_hash)


@client.on(events.NewMessage(chats=(chat_id)))
async def normal_handler(event):
    user_mess=event.message.to_dict()['message'].replace("\n","")
    api_play_music = PlayMusic()
    track_id = Messages.get_track_id(user_mess)
    temp_play_list_name = Messages.get_play_list(user_mess)
    if track_id:  
        temp_play_list_name = Messages.get_play_list(user_mess)
        struct = MessageStruct(track_id, temp_play_list_name)
        f.write("Default == " + play_list_name + " - Finded play_list == " + temp_play_list_name + "\n\n")
        set_songs = set()
        set_songs.add(struct)
        api_play_music.add_set_song_to_play_list(play_list_name, set_songs)
        set_new_play_lists = api_play_music.get_new_play_lists()
        if(len(set_new_play_lists) > 0):
            for new_play_list in set_new_play_lists:
                await client.send_message(chat_id, play_list_created + play_music_play_list_url + new_play_list)
        f.write(user_mess+"\n\n")
        f.flush()

    if not (track_id) and temp_play_list_name:
        play_list = api_play_music.find_play_list(temp_play_list_name)
        if play_list is None:
            pass
        else:
            await client.send_message(chat_id, play_music_play_list_url + play_list["id"])

client.start()
f=open('messages_from_chat', 'a') 

client.run_until_disconnected()
f.close()
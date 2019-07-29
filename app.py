from core import *

chat_id = "MaryBakhtina"
#chat_id = "katyn_katun"
play_list_name = "Telegram music"
min_message = 0


def add_songs_to_play_list():
    api_play_music = PlayMusic()
    messages = Messages(chat_id, min_message)

    message_struct = messages.get_songs()
    api_play_music.add_set_song_to_play_list(play_list_name, message_struct)

add_songs_to_play_list()

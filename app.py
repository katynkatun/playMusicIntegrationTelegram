from core import *

chat_id = "MaryBakhtina"
#chat_id = "katyn_katun"
play_list_name = "test"
min_message = 0


def add_songs_to_play_list():
    api_play_music = PlayMusic()
    messages = Messages(chat_id, min_message)

    set_songs = messages.get_songs()
    api_play_music.add_setsong_to_play_list(play_list_name, set_songs)

add_songs_to_play_list()
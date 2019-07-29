import unittest
from core.telegram import Messages

not_found = "https://play.google.com/music/m/Tbkwks3eah7p2i5lt3f6jcziwee?t=The_Way_God_Made_Me_-_MAGIC"
found_one_first_and_split = "#Test https://play.google.com/music/m/Tbkwks3eah7p2i5lt3f6jcziwee?t=The_Way_God_Made_Me_-_MAGIC"
found_one_first_and_not_split = "#Testhttps://play.google.com/music/m/Tbkwks3eah7p2i5lt3f6jcziwee?t=The_Way_God_Made_Me_-_MAGIC"
found_some_text_first = "Some text #Test  sds https://play.google.com/music/m/Tbkwks3eah7p2i5lt3f6jcziwee?t=The_Way_God_Made_Me_-_MAGIC"
found_some_text_first_long_name = "Some text #'Test  sds' https://play.google.com/music/m/Tbkwks3eah7p2i5lt3f6jcziwee?t=The_Way_God_Made_Me_-_MAGIC"
not_found_play_list_simvol = "Some text 'Test  sdshttps://play.google.com/music/m/Tbkwks3eah7p2i5lt3f6jcziwee?t=The_Way_God_Made_Me_-_MAGIC"
not_found_play_end_long_name = "Some text #'Test  sdshttps://play.google.com/music/m/Tbkwks3eah7p2i5lt3f6jcziwee?t=The_Way_God_Made_Me_-_MAGIC"
found_Telegrma = f'#Telegram https://play.google.com/music/m/To56bcdfd4232ttniog3mlwzhu4?t=Doom_Days_-_Bastille'
found_at_the_end = "https://play.google.com/music/m/Tyeq6ovhyn6yq4isvylcbjknkpa?t=Put_It_On_Me_-_Matt_Maeson#Telegram1"



class TestGetPlaylist(unittest.TestCase):
    
    def test_not_found(self):
        self.assertEqual(Messages.get_play_list(not_found), "")

    def test_found_one_first_and_split(self):
        self.assertEqual(Messages.get_play_list(found_one_first_and_split), "Test")

    def test_found_one_first_and_not_split(self):
        self.assertEqual(Messages.get_play_list(found_one_first_and_not_split), "Test")

    def test_found_some_text_first(self):
        self.assertEqual(Messages.get_play_list(found_some_text_first), "Test")

    def test_found_some_text_first_long_name(self):
        self.assertEqual(Messages.get_play_list(found_some_text_first_long_name), "Test  sds")

    def test_not_found_play_list_simvol(self):
        self.assertEqual(Messages.get_play_list(not_found_play_list_simvol), "")

    def test_not_found_play_end_long_name(self):
        self.assertEqual(Messages.get_play_list(not_found_play_end_long_name), "")

    def test_found_Telegram(self):
        self.assertEqual(Messages.get_play_list(found_Telegrma), "Telegram")
    
    def test_found_at_the_and_Telegram1(self):
        self.assertEqual(Messages.get_play_list(found_at_the_end), "Telegram1")

if __name__ == '__main__':
    unittest.main()
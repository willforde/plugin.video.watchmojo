import unittest

# Testing specific imports
from codequick import youtube
import codequick
from addon import main as addon

# Check witch version of codequick we are running
framework_version = codequick.__dict__.get("__version__", (0, 9, 0))


class Tester(unittest.TestCase):
    def test_root(self):
        data = addon.root.test()
        self.assertGreaterEqual(len(data), 20)

    def test_youtube_channel_watchmojo(self):
        data = youtube.Playlist.test("UCaWd5_7JhbQBe4dknZhsHJg")
        self.assertGreaterEqual(len(data), 50)

    def test_youtube_channel_watchmojo_uk(self):
        data = youtube.Playlist.test("UCMm0YNfHOCA-bvHmOBSx-ZA")
        self.assertGreaterEqual(len(data), 50)

    def test_video_list_music(self):
        data = addon.video_list.test("http://www.watchmojo.com/categories/Music")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_tv(self):
        data = addon.video_list.test("http://www.watchmojo.com/categories/TV")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_facts(self):
        data = addon.video_list.test("/shows/WMFacts")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_myths(self):
        data = addon.video_list.test("/shows/WMMyths")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_news(self):
        data = addon.video_list.test("/shows/WMNews")
        self.assertGreaterEqual(len(data), 30)

    def test_video_list_games(self):
        data = addon.video_list.test("/categories/video games")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_mojo(self):
        data = addon.video_list.test("/msmojo/")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_next(self):
        data = addon.video_list.test("/categories/music/2")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_tags(self):
        data = addon.video_list.test("/tag/Film/1")
        self.assertGreaterEqual(len(data), 40)

    def test_related(self):
        data = addon.related.test("http://www.watchmojo.com/video/id/19541/")
        self.assertGreaterEqual(len(data), 12)

    def test_tags(self):
        data = addon.tags.test("http://www.watchmojo.com/video/id/19541/")
        self.assertGreaterEqual(len(data), 5)

    @unittest.skip
    def test_play_video_type1(self):
        ret = addon.play_video.test(u"https://www.watchmojo.com/video/id/19268/")
        self.assertEqual(ret, u"plugin://plugin.video.youtube/play/?video_id=Fi2qpF2q5vk")

    @unittest.skip
    def test_play_video_type2(self):
        ret = addon.play_video.test(u"https://www.watchmojo.com/video/id/20838/")
        self.assertEqual(ret, u"plugin://plugin.video.youtube/play/?video_id=P3PvFiCibts")

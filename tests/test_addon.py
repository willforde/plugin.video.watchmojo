from addondev import initializer
import os

initializer(os.path.dirname(os.path.dirname(__file__)))
import unittest
import addon
from codequick import youtube


class Tester(unittest.TestCase):
    def test_root(self):
        data = addon.root.test()
        self.assertGreaterEqual(len(data), 20)

    def test_youtube_channel(self):
        data = youtube.Playlists.test("UCaWd5_7JhbQBe4dknZhsHJg")
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

    def test_video_list_mojo(self):
        data = addon.video_list.test("/msmojo/")
        self.assertGreaterEqual(len(data), 40)

    def test_video_list_next(self):
        data = addon.video_list.test("/categories/music/2")
        self.assertGreaterEqual(len(data), 40)

    def test_related(self):
        data = addon.related.test("http://www.watchmojo.com/video/id/19541/")
        self.assertGreaterEqual(len(data), 12)

    def test_tags(self):
        data = addon.tags.test("http://www.watchmojo.com/video/id/19541/")
        self.assertGreaterEqual(len(data), 5)

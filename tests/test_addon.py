import unittest

# Testing specific imports
from codequick import youtube


class Tester(unittest.TestCase):
    def test_youtube_channel_watchmojo(self):
        data = youtube.Playlist.test("UCaWd5_7JhbQBe4dknZhsHJg")
        self.assertGreaterEqual(len(data), 50)

    def test_youtube_channel_watchmojo_uk(self):
        data = youtube.Playlist.test("UCMm0YNfHOCA-bvHmOBSx-ZA")
        self.assertGreaterEqual(len(data), 50)

    def test_youtube_channel_mojotravels(self):
        data = youtube.Playlist.test("UC9_eukrzdzY91jjDZm62FXQ")
        self.assertGreaterEqual(len(data), 50)

    def test_youtube_channel_mojoplays(self):
        data = youtube.Playlist.test("UC4HnC-AS714lT2TCTJ-A1zQ")
        self.assertGreaterEqual(len(data), 50)

    def test_youtube_channel_MojoTalks(self):
        data = youtube.Playlist.test("UC88y_sxutS1mnoeBDroS74w")
        self.assertGreaterEqual(len(data), 50)

    def test_youtube_channel_msmojo(self):
        data = youtube.Playlist.test("UC3rLoj87ctEHCcS7BuvIzkQ")
        self.assertGreaterEqual(len(data), 50)

    def test_youtube_channel_unveiled(self):
        data = youtube.Playlist.test("UCYJyrEdlwxUu7UwtFS6jA_Q")
        self.assertGreaterEqual(len(data), 50)

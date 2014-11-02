import unittest
import os.path
from models.song import Song
from models.song_queue import SongQueue


class Tests_SongQueue(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("path1")
        self.song2 = Song("path2")
        self.song3 = Song("path3")
        self.song4 = Song("path4")

    def tearDown(self):
        return

    def test_init(self):
        self.queue = SongQueue(self.song1)
        self.assertEqual(self.queue.get_current(), self.song1)

    def test_nonzero(self):
        queue = SongQueue()
        self.assertFalse(queue)
        queue = SongQueue(self.song1)
        self.assertTrue(queue)

    def test_add_last(self):
        self.test_init()
        self.queue.add_last(self.song3)

        while self.queue.has_next():
            self.queue.get_next()

        self.assertEqual(self.queue.get_current(), self.song3)

if __name__ == '__main__':
    unittest.main()

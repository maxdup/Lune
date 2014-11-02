import unittest
import os.path
from models.song import Song
from models.song_queue import SongQueue


class Tests_SongQueue(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("path1")
        self.song2 = Song("path2")
        self.song3 = Song("path3")
        self.queue = SongQueue()

    def tearDown(self):
        return

    def testqueue_add_last(self):
        self.assertTrue(not self.queue)
        self.assertTrue(not self.queue.has_index(0))

        self.queue.add_last(self.song1)

        self.assertTrue(self.queue)
        self.assertTrue(len(self.queue) == 1)
        self.assertTrue(self.queue.has_index(0))
        self.assertTrue(not self.queue.has_index(1))

        self.queue.add_last([self.song2, self.song3])

        self.assertTrue(len(self.queue) == 3)
        self.assertTrue(self.queue.has_index(1))
        self.assertTrue(self.queue.has_index(2))
        self.assertTrue(not self.queue.has_index(3))

if __name__ == '__main__':
    unittest.main()

import os
import unittest

from reader.csv_reader import CsvReader


class CsvReaderTest(unittest.TestCase):

    def test_run(self):
        reader = CsvReader(os.curdir)
        actual = reader.read(os.path.join('test', 'data', 'd1.csv'), {})
        self.assertIsNotNone(actual)
        self.assertEquals((4, 2), actual.shape)

import os
import unittest

from merger import Merger


class MergerTest(unittest.TestCase):

    def test_run(self):
        merger = Merger()
        actual = merger.run(os.path.join('test', 'data', 'cfg.csv'))
        self.assertIsNotNone(actual)
        self.assertIs(3, actual.shape[1])

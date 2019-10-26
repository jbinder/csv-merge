import os
import unittest

from reader.xls_reader import XlsReader


class XlsReaderTest(unittest.TestCase):

    def test_run(self):
        reader = XlsReader(os.curdir)
        actual = reader.read(os.path.join('test', 'data', 'e1.xlsx'), {'header': None})
        self.assertIsNotNone(actual)
        self.assertEquals((3, 1), actual.shape)

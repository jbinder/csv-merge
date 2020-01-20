import os
import unittest

from preprocessor.time_series_preprocessor import TimeSeriesPreprocessor
from reader.csv_reader import CsvReader


class TimeSeriesPreprocessorTest(unittest.TestCase):

    def test_process_include_2_previous_entries_should_reshape_data(self):
        reader = CsvReader(os.curdir)
        data = reader.read(os.path.join('test', 'data', 'd1.csv'), {})
        preprocessor = TimeSeriesPreprocessor()
        actual = preprocessor.process(data, {'num_previous_entries_to_include': 2})
        self.assertIsNotNone(actual)
        self.assertEquals((2, 4), actual.shape)

    def test_process_include_no_previous_entries_should_not_reshape_data(self):
        reader = CsvReader(os.curdir)
        data = reader.read(os.path.join('test', 'data', 'd1.csv'), {})
        preprocessor = TimeSeriesPreprocessor()
        actual = preprocessor.process(data, {'num_previous_entries_to_include': 0})
        self.assertIsNotNone(actual)
        self.assertEquals((4, 2), actual.shape)

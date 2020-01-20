import pandas as pd

from preprocessor.preprocessor import Preprocessor


class TimeSeriesPreprocessor(Preprocessor):
    def process(self, data: pd.DataFrame, options: map) -> pd.DataFrame:
        num_previous_entries_to_include = options['num_previous_entries_to_include']
        result = data
        if num_previous_entries_to_include > 0:
            self.append_previous_data_as_column(data, num_previous_entries_to_include)
            result = data[:-num_previous_entries_to_include]  # drop incomplete rows
        return result

    @staticmethod
    def append_previous_data_as_column(data, num_previous_entries_to_include):
        columns = data.columns[1:]
        for column in columns:
            for i in range(1, num_previous_entries_to_include + 1):
                data[column + f" -{i}"] = data.shift(-i)[column]

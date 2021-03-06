import os
from os.path import dirname
from typing import Tuple, List

import pandas as pd

from reader.csv_reader import CsvReader
from reader.xls_reader import XlsReader


class Merger:

    def __init__(self):
        self.reader = {'csv': CsvReader(os.curdir),
                       'xlsx': XlsReader(os.curdir)}

    def run(self, config_file: str) -> pd.DataFrame:
        base_dir = os.getcwd()
        cfg = pd.read_csv(os.path.join(base_dir, config_file))
        common_keys, csvs = self._prepare_csvs(base_dir, cfg, config_file)
        result = self._build_result(cfg, common_keys, csvs)
        result.columns = pd.concat([pd.Series(['id']), cfg[cfg.columns[0]]])
        return result

    def _build_result(self, cfg: pd.DataFrame, common_keys: pd.Index, csvs: [pd.DataFrame]) -> pd.DataFrame:
        common_keys = common_keys.sort_values(ascending=False)
        result = pd.DataFrame(common_keys)
        for index, row in cfg.iterrows():
            id_column = row[1]
            id_column_name = self._get_column_name(csvs[index], id_column)
            data_column = row[2]
            data = csvs[index].query(f"`{id_column_name}` in @common_keys")
            data = data.sort_values(by=id_column_name, ascending=False)
            data = pd.Series(data.iloc[:, data_column].values)
            result = pd.concat([result, data], axis=1)
        result = result.dropna()
        return result

    def _prepare_csvs(self, base_dir: str, cfg: pd.DataFrame, config_file: str) -> Tuple[pd.Index, List[pd.DataFrame]]:
        csvs = []
        common_keys = pd.Index([])
        for index, row in cfg.iterrows():
            id_column = row[1]
            id_type = row[3]
            file_name = os.path.join(dirname(config_file), row[0])
            csv = self.reader[os.path.splitext(file_name)[1][1:]].read(file_name)
            if id_type == 'datetime':
                id_column_name = self._get_column_name(csv, id_column)
                csv[id_column_name] = pd.to_datetime(csv[id_column_name], errors='coerce')
            keys = pd.Index(csv.iloc[:, id_column]).dropna()
            if common_keys.shape[0] > 0:
                common_keys = keys.intersection(common_keys)
            else:
                common_keys = keys
            csvs.append(csv)
        return common_keys, csvs

    @staticmethod
    def _get_column_name(df: pd.DataFrame, index: int):
        return df.keys()[index]

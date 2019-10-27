import os
from os.path import dirname
from typing import Tuple, List

import pandas as pd

from reader.csv_reader import CsvReader
from reader.xls_reader import XlsReader


class Merger:

    def __init__(self):
        self.reader = {'csv': CsvReader(os.curdir)}
        self.reader = {'xlsx': XlsReader(os.curdir)}

    def run(self, config_file: str) -> pd.DataFrame:
        base_dir = os.getcwd()
        cfg = pd.read_csv(os.path.join(base_dir, config_file))
        common_keys, csvs = self._prepare_csvs(base_dir, cfg, config_file)
        result = self._build_result(cfg, common_keys, csvs)
        return result

    def _build_result(self, cfg: pd.DataFrame, common_keys: pd.Index, csvs: [pd.DataFrame]) -> pd.DataFrame:
        result = pd.DataFrame(common_keys)
        for index, row in cfg.iterrows():
            id_column = row[1]
            id_column_name = csvs[index].keys()[id_column]
            data_column = row[2]
            data = csvs[index].query(f"`{id_column_name}` in @common_keys")
            data = data.sort_values(by=id_column_name)
            data = pd.Series(data.iloc[:, data_column].values)
            result = pd.concat([result, data], axis=1)
        return result

    def _prepare_csvs(self, base_dir: str, cfg: pd.DataFrame, config_file: str) -> Tuple[pd.Index, List[pd.DataFrame]]:
        csvs = []
        common_keys = pd.Index([])
        for index, row in cfg.iterrows():
            file_name = os.path.join(dirname(config_file), row[0])
            id_column = row[1]
            csv = self.reader[os.path.splitext(file_name)[1][1:]].read(file_name)
            keys = pd.Index(csv.iloc[:, id_column])
            if common_keys.any():
                common_keys = keys.intersection(common_keys)
            else:
                common_keys = keys
            csvs.append(csv)
        return common_keys, csvs

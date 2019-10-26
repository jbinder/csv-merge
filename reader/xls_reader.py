import os

import pandas as pd

from reader.reader import Reader


class XlsReader(Reader):
    def __init__(self, base_dir: str):
        super().__init__()
        self.base_dir = base_dir

    def read(self, file_name: str, options: dict = None) -> pd.DataFrame:
        return pd.read_excel(os.path.join(self.base_dir, file_name), **options)

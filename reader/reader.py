import abc
import string

import pandas as pd


class Reader(abc.ABC):
    @abc.abstractmethod
    def read(self, file_name: string, options: dict = None) -> pd.DataFrame:
        pass

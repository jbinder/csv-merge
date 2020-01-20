import abc
import pandas as pd


class Preprocessor(abc.ABC):
    @abc.abstractmethod
    def process(self, data: pd.DataFrame, options: map) -> pd.DataFrame:
        pass

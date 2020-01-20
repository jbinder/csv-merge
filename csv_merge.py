import argparse

from merger import Merger
from preprocessor.time_series_preprocessor import TimeSeriesPreprocessor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merges multiple CSV-files.')
    parser.add_argument('--config_file', action="store", default="cfg.csv")
    parser.add_argument('--result_file', action="store", default="merged.csv")
    parser.add_argument('--num_previous_entries_to_include', action="store", type=int, default=0)
    args = parser.parse_args()
    df = Merger().run(args.config_file)
    df = TimeSeriesPreprocessor().process(df, {'num_previous_entries_to_include': args.num_previous_entries_to_include})
    df.to_csv(args.result_file, index=False)

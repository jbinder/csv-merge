import argparse

from merger import Merger

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merges multiple CSV-files.')
    parser.add_argument('--config_file', action="store", default="cfg.csv")
    parser.add_argument('--result_file', action="store", default="merged.csv")
    args = parser.parse_args()
    merged = Merger().run(args.config_file)
    merged.to_csv(args.result_file, index=False)

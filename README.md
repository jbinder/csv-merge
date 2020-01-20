csv-merge
=========

Merges several individual CSV files to one, thereby extracting a data column and matching those using an index column.
Currently supports the data type as index column.

:warning: Work in progress!


Requirements
------------

- Python 3.6


Setup
-----

    pip install -r requirements.txt


Usage
-----

The configuration is read from a config file and is a CSV file itself, using the columns filename, index column, data column.

Example (cfg.csv):

    filename,key_column,data_column,key_type
    d1.csv,0,1,int
    d2.csv,0,2,datetime

where:

* key_type: int | str | datetime

Run using:

    python csv_merge.py --config_file test/data/cfg.csv --result_file  merged.csv --num_previous_entries_to_include

Arguments:

* config_file: The configuration file as described above.
* result file: The merged CSV file.
* num_previous_entries_to_include: Optional. Allows copying elements from x previous rows to include a history for e.g. time series.

Tests
-----

Run the tests using:

    nosetests

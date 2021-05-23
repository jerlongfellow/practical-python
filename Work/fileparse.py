# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_header=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_header:
        raise RuntimeError('select argument requires column headers')
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if has_header:
            headers = next(rows)

        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
        else:
            indices = []

        records = []
        for row_number, row in enumerate(rows, start=1):
            if not row:
                continue

            try:
                if indices:
                    row = [ row[index] for index in indices ]

                if types:
                    row = [ func(val) for func, val in zip(types, row) ]

                record = dict(zip(headers, row)) if has_header else tuple(row)
                records.append(record)
            except ValueError as e:
                print(f"Row {row_number}: Couldn't convert {row}")
                print(f'Row {row_number}: Reason {e}')

    return records

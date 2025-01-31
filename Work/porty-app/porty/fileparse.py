# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(file, select=None, types=None, has_header=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_header:
        raise RuntimeError('select argument requires column headers')

    if isinstance(file, str):
        raise TypeError('file should be Iterable[str], not str')

    rows = csv.reader(file, delimiter=delimiter)

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
            if not silence_errors:
                log.warning(f"Row %d: Couldn't convert %s", row_number, row)
                log.debug(f'Row %d: Reason %s', row_number, e)
            continue

    return records

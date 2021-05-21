# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.00
    with open(filename, 'rt') as portfolio_file:
        rows = csv.reader(portfolio_file)
        headers = next(rows)
        for row_number, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                num_shares = int(record['shares'])
                share_price = float(record['price'])
                total_cost += num_shares * share_price
            except ValueError:
                print(f"Row {row_number}: Couldn't convert: {row}")
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')

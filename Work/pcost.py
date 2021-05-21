# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.00
    with open(filename, 'rt') as portfolio_file:
        rows = csv.reader(portfolio_file)
        next(rows)
        for row in rows:
            try:
                num_shares = int(row[1])
                share_price = float(row[2])
            except ValueError:
                print(f'could not process {row}')
            total_cost += num_shares * share_price
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')

# pcost.py
#
# Exercise 1.27

from report import read_portfolio
import sys


def portfolio_cost(filename):
    total_cost = 0.00
    portfolio = read_portfolio(filename)

    for holding in portfolio:
        total_cost += holding['shares'] * holding['price']

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')

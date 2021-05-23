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


def main(argv):
    print(f'Total cost: {portfolio_cost(argv[1]):.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)

# no change needed for Exercise 3.16

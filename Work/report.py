# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from stock import Stock


def read_portfolio(filename):
    with open(filename, 'rt') as file:
        holdings = parse_csv(file, types=[str, int, float])
        portfolio = [
            Stock(holding['name'], holding['shares'], holding['price'])
            for holding in holdings
        ]

    return portfolio


def read_prices(filename):
    with open(filename, 'rt') as file:
        prices = dict(parse_csv(file, types=[str, float], has_header=False))

    return prices


def make_report(portfolio, prices):
    report = []

    for holding in portfolio:
        name = holding.name
        shares = holding.shares
        price = prices[name]
        change = price - holding.price
        
        report.append((name, shares, price, change))

    return report


def print_report(report, headers=('Name', 'Shares', 'Price', 'Change')):
    header_string = ''
    separator_string = ''

    for header in headers:
        header_string += f'{header:>10s} '
        separator_string += '-' * 10 + ' '

    print(header_string[:-1])
    print(separator_string[:-1])

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {f"${price:0.2f}":>10} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    print_report(make_report(
        read_portfolio(portfolio_filename),
        read_prices(prices_filename)
    ))
    

def main(argv):
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)

# no change needed for Exercise 3.16

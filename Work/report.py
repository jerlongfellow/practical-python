# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename):
    return parse_csv(filename, types=[str, int, float])


def read_prices(filename):
    return dict(parse_csv(filename, types=[str, float], has_header=False))


def make_report(portfolio, prices):
    report = []

    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = prices[name]
        change = price - holding['price']
        
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
    
portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name'   : row[0],
                'shares' : int(row[1]),
                'price'  : float(row[2])
            }
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'Could not add {row} to prices.')

    return prices

def make_report(portfolio, prices):
    report = []

    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = prices[name]
        change = price - holding['price']
        
        report.append((name, shares, price, change))

    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
current_portfolio_value = 0.0
gain = 0.0

for holding in portfolio:
    current_holding_value = prices[holding['name']] * holding['shares']
    original_holding_value = holding['shares'] * holding['price']
    current_portfolio_value += current_holding_value
    gain += current_holding_value - original_holding_value

print(f'Current value of the portfolio: {current_portfolio_value}')
print(f'Gain/loss: {gain}')

headers = ('Name', 'Shares', 'Price', 'Change')
report = make_report(portfolio, prices)

header_string = ''
separator_string = ''

for header in headers:
    header_string += f'{header:>10s} '
    separator_string += '-' * 10 + ' '

print(header_string[:-1])
print(separator_string[:-1])

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

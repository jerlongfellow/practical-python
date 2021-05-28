# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat


def read_portfolio(filename):
    with open(filename, 'rt') as file:
        holdings = parse_csv(file, types=[str, int, float])
        portfolio = [ Stock(**holding) for holding in holdings ]

    return Portfolio(portfolio)


def read_prices(filename):
    with open(filename, 'rt') as file:
        prices = dict(parse_csv(file, types=[str, float], has_header=False))

    return prices


def make_report_data(portfolio, prices):
    report = []

    for holding in portfolio:
        name = holding.name
        shares = holding.shares
        price = prices[name]
        change = price - holding.price
        
        report.append((name, shares, price, change))

    return report


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    

def main(argv):
    if len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)

# no change needed for Exercise 3.16

from follow import follow
import tableformat
import report
import csv

class Ticker:
    def __init__(self, tickerdict):
        self.Name = tickerdict['name']
        self.Price = tickerdict['price']
        self.Change = tickerdict['change']


def select_columns(rows, indices):
    return ([row[index] for index in indices] for row in rows)


def convert_types(rows, types):
    return ([func(val) for func, val in zip(types, row)] for row in rows)


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def make_tickers(tickerdicts):
    return (Ticker(tickerdict) for tickerdict in tickerdicts)


def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    formatter = tableformat.create_formatter(fmt)
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    rows = make_tickers(rows)
    tableformat.print_table(rows, ['Name', 'Price', 'Change'], formatter)


if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)

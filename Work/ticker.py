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
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def make_tickers(tickerdicts):
    for tickerdict in tickerdicts:
        yield Ticker(tickerdict)


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


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

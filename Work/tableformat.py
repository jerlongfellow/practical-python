class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for datum in rowdata:
            print(f'{datum:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(self.make_table_row(headers, cell_type='h'))

    def row(self, rowdata):
        print(self.make_table_row(rowdata))

    def make_table_row(self, data, cell_type='d'):
        return '<tr>' + ''.join([ f'<t{cell_type}>{datum}</t{cell_type}>' for datum in data ]) + '</tr>'


names_to_formatters = {
    'txt' : TextTableFormatter,
    'csv' : CSVTableFormatter,
    'html' : HTMLTableFormatter
}

def create_formatter(name):
    return names_to_formatters[name]()

def print_table(objs, attrs, formatter):
    formatter.headings(attrs)
    for obj in objs:
        formatter.row([ str(getattr(obj, attr)) for attr in attrs ])

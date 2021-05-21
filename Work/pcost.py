# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    total_cost = 0.00
    with open(filename, 'rt') as portfolio_file:
        next(portfolio_file)
        for line in portfolio_file:
            split_line = line.split(',')
            try:
                num_shares = int(split_line[1])
                share_price = float(split_line[2])
            except ValueError:
                print(f'could not process {line}')
            total_cost += num_shares * share_price
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost:.2f}')

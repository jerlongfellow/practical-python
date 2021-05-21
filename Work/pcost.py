# pcost.py
#
# Exercise 1.27

total_cost = 0.00

with open('Data/portfolio.csv', 'rt') as portfolio_file:
    next(portfolio_file)
    for line in portfolio_file:
        split_line = line.split(',')
        num_shares = int(split_line[1])
        share_price = float(split_line[2])
        total_cost += num_shares * share_price

print(f'Total cost {total_cost:.2f}')

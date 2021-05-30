from .typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, sold_shares: int):
        if self.shares < sold_shares:
            raise RuntimeError('Cannot sell more shares than are currently held.')
        else:
            self.shares -= sold_shares

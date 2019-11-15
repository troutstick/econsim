class Transanction:
    def __init__(self, resource, bid_price, transaction_amount):
        self.resource = resource
        self.bid_price = bid_price
        self.transaction_amount = transaction_amount


class Buy(Transanction):
    def __init__(self, resource, bid_price, buy_amount):
        Transanction.__init__(self, resource, bid_price, buy_amount)

class Sell(Transanction):
    def __init__(self, resource, bid_price, buy_amount):
        Transanction.__init__(self, resource, bid_price, buy_amount)

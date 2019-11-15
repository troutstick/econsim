import pops
import marketplace

class Transaction:
    """Representation of offers for buying/selling resources."""
    def __init__(self, bidder, resource, bid_price, transaction_amount):
        self.bidder = bidder
        self.resource = resource
        self.bid_price = bid_price
        self.transaction_amount = transaction_amount


class Buy(Transaction):
    def __init__(self, bidder, resource, bid_price, buy_amount):
        Transaction.__init__(self, bidder, resource, bid_price, buy_amount)

class Sell(Transaction):
    def __init__(self, bidder, resource, bid_price, buy_amount):
        Transaction.__init__(self, bidder, resource, bid_price, buy_amount)

def perform_transaction(buy, sell):
    """A buy and a sell are compared; a transaction is performed if they are agreeable"""

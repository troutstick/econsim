import pops
import marketplace

class Transaction:
    """Representation of offers for buying/selling resources."""
    def __init__(self, bidder, resource_name, bid_price, amount):
        self.bidder = bidder
        self.resource_name = resource_name
        self.bid_price = bid_price
        self.amount = amount


class Buy(Transaction):
    def __init__(self, bidder, resource_name, bid_price, buy_amount):
        Transaction.__init__(self, bidder, resource_name, bid_price, buy_amount)

class Sell(Transaction):
    def __init__(self, bidder, resource_name, bid_price, sell_amount):
        Transaction.__init__(self, bidder, resource_name, bid_price, sell_amount)



def perform_transaction(marketplace, buy, sell):
    """A buy and a sell are compared; a transaction is performed if they are agreeable.
    The CLEARING_PRICE is based on the mean of the BID_PRICE of both the Buy and the Sell.

    Reports how much of resource and money was exchanged.
    """
    if buy.bid_price >= sell.bid_price:
        resource_amount = min(buy.amount, sell.amount)
        resource_name = buy.resource_name
        clearing_price = (buy.bid_price + sell.bid_price) / 2
        total_price = resource_amount * clearing_price
        buyer = buy.bidder
        seller = sell.bidder

        buyer.exchange(resource_name, resource_amount, -total_price)
        seller.exchange(resource_name, -resource_amount, total_price)
        marketplace.exchange(resource_name, resource_amount, total_price)
    else:
        raise NoTransactionException('Buyer and seller unable to agree to a deal.')

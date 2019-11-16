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

def perform_transaction(buy, sell):
    """A buy and a sell are compared; a transaction is performed if they are agreeable.
    The transaction price is based on the BID_PRICE of the Sell instance.
    """
    def transaction_success():
        """A helper function that returns True/False depending on whether or not
        the parties agree to the transaction.

        WIP

        Works by comparing info contained in BUY and SELL.
        """
        return True

    if transaction_success():
        resource_amount = min(buy.amount, sell.amount)
        resource_name = buy.resource_name
        total_price = resource_amount * sell.bid_price
        buyer = buy.bidder
        seller = sell.bidder
        buyer.add_to_inventory(resource_name, resource_amount)
        buyer.add_cash(-total_price)
        seller.add_to_inventory(resource_name, -resource_amount)
        seller.add_cash(total_price)

    else:
        raise NoTransactionException('Buyer and seller unable to agree to a deal.')

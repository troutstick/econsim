import random
import pops
import transactions

class Marketplace:
    """Where money is exchanged for goods and services.

    Each market has a price for each type of RESOURCE, and updates prices based on how much was bought vs sold."""
    def __init__(self, agents, allowed_resources):
        """Agents are actors that act in the economy. Can be pops or whole nations."""
        self.agents = agents
        self.allowed_resources = allowed_resources # list of all resources that can be traded here
        self.buy_list = []      # bids and asks
        self.sell_list = []

    def simulate_market(self):
        """The invisible hand of the free market simulates the passing of a day."""
        self.perform_production()
        self.generate_offers()
        self.resolve_offers()

    def perform_production(self):
        """Various resources are produced/consumed."""
        for agent in agents:
            agent.produce()

    def generate_offers(self):
        """Agents offer up items in the marketplace to be sold."""
        for agent in agents:
            agent.offer()

    def resolve_offers(self):
        """Willing buyers and sellers perform transactions."""
        transaction_key = lambda transaction: transaction.bid_price
        sorted_buy_list = buy_list.sort(key=transaction_key, reverse=True) # buys are sorted in descending order
        sorted_sell_list = sell_list.sort(key=transaction_key)
        try:
            while sorted_buy_list and sorted_sell_list:
                perform_transaction(sorted_buy_list.pop(0), sorted_sell_list.pop(0))
            return
        except NoTransactionException:
            return

    def add_bid(bid):
        """Adds a buy or sell bid to the marketplace."""
        if bid is None:
            return
        elif isinstance(bid, Buy):
            buy_list.append(bid)
        elif isinstance(bid, Sell):
            sell_list.append(bid)


        #class Lower_Class(Pop):
        """Represents people in the lower echelons of society."""

        #class Middle_Class(Pop):
        """Represents people in the middle echelons of society."""

        #class Upper_Class(Pop):
        """Represents people in the upper echelons of society."""

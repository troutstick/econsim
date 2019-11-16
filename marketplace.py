import random
import pops
import transactions

class Marketplace:
    """Where money is exchanged for goods and services.

    Each market has a price for each type of RESOURCE, and updates prices based on how much was bought vs sold.
    """
    def __init__(self, name, agents, allowed_resources):
        """Agents are actors that act in the economy. Can be pops or whole nations."""
        self.name = name
        self.agents = agents
        self.allowed_resources = allowed_resources # list of all resources that can be traded here
        self.market_reset() # prepare for new trading round

    #########################
    # Interfaces to interact with marketplace
    #########################


    def get_clearing_price(self, resource_name):
        """Looks up the average clearing price of a resource as of the most recent trading round."""
        return self.clearing_prices.get(resource_name)

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
        for resource_name in self.allowed_resources:
            self.resolve_for_resource(resource_name)
            self.update_clearing_price(resource_name)
            self.market_reset()

    def resolve_for_resource(self, resource_name):
        """Resolves outstanding transactions of a specific resource type."""
        transaction_key = lambda transaction: transaction.bid_price

        resource_buy_list = [buy for buy in self.buy_list if buy.resource_name == resource_name]
        resource_sell_list = [sell for sell in self.sell_list if sell.resource_name == resource_name]
        sorted_buy_list = resource_buy_list.sort(key=transaction_key, reverse=True) # buys are sorted in descending order
        sorted_sell_list = resource_sell_list.sort(key=transaction_key)

        try:
            while sorted_buy_list and sorted_sell_list:
                perform_transaction(self, sorted_buy_list.pop(0), sorted_sell_list.pop(0))
            return
        except NoTransactionException:
            return

    def market_reset(self):
        """Resets stuff for a new trading round."""
        self.buy_list = []      # bids and asks
        self.sell_list = []
        self.clearing_prices = [] # each resource's clearing price at this market

        # used to update clearing prices every day
        self.material_exchanged = 0
        self.money_exchanged = 0

    def exchange(self, resource_name, resource_amount, cash_amount):
        """Helps to update clearing price; updates the amount of cash/material exchanged in a trading round."""
        self.material_exchanged += resource_amount
        self.money_exchanged += cash_amount

    def update_clearing_price(self, resource_name):
        """Updates the average price per unit of material sold during a trading round."""
        self.clearing_price[resource_name] = self.money_exchanged / self.material_exchanged

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

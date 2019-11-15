import random
import pops

class Marketplace:
    """Where money is exchanged for goods and services.

    Each market has a price for each type of RESOURCE, and updates prices based on how much was bought vs sold."""
    def __init__(self, agents):
        """Agents are actors that act in the economy. Can be pops or whole nations."""
        self.agents = agents
        self.buy_list = []
        self.sell_list = []

    def buy(self, agents):
        """All agents offer up items in the marketplace to be sold."""

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

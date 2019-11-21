import random

class Pop:
    """Class representing all people."""
    def __init__(self, marketplace, needs, money, inventory):
        """NEEDS is a dictionary: pairing up a type of material with how much they desire to buy/sell them."""
        #self.size = size
        #self.ethnicity = ethnicity
        #self.religion = religion
        self.marketplace = marketplace
        self.needs = needs
        self.money = money
        self.inventory = inventory

    def needs(self, resource_name, curr_price):
        """The AI function: The pop tries to fulfill its daily desires.

        resource_name = the type of resource being interacted with
        ideal_amount = how much the pop wants to buy/sell
        curr_amount = how much of this resource_name that this pop owns
        curr_price = the price of this resource_name in the pop's marketplace"""

        curr_amount = self.inventory.get(resource_name)
        ideal_amount = self.needs.get(resource_name)
        if ideal_amount > curr_amount:
            self.create_buy(resource_name, ideal_amount, curr_price)
        elif ideal_amount < curr_amount:
            self.create_sell(resource_name, ideal_amount, curr_price)

    def create_buy(self, resource):
        """Returns an offer to buy a good at the marketplace"""
        bid_price = resource.price
        buy_amount = amount_to_buy(self, resource)
        return min(buy_amount, )

    def create_sell(self):
        """Returns an offer to sell a good at the marketplace"""
        pass

    def amount_to_buy(self, resource):
        """Return how much of resource that the pop wants to buy.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transanctions that the pop has seen
        DEFICIT = how much of RESOURCE it would take to get to ideal_amount
        """
        mean = resource.mean
        favorability =
        deficit = self.needs.get(resource_name) - self.inventory.get(resource_name)
        return favorability * deficit

    def amount_to_sell(self, resource):
        """Return how much of resource that the pop wants to sell.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transanctions that the pop has seen
        EXCESS = how much of RESOURCE is in the inventory
        """
        mean = resource.mean
        favorability =
        excess = self.inventory.get(resource_name) - self.needs.get(resource_name)
        return favorability * excess

    def update_price(self):
        """Method to update the prices that the pop expects to encounter in its marketplace."""
        pass


#class Lower_Class(Pop):
    """Represents people in the lower echelons of society."""

#class Middle_Class(Pop):
    """Represents people in the middle echelons of society."""

#class Upper_Class(Pop):
    """Represents people in the upper echelons of society."""

class Marketplace:
    """Where money is exchanged for goods and services."""
    def __init__(self, agents):
        """Agents are actors that act in the economy. Can be pops or whole nations."""
        self.agents = agents

    def buy(self, agents):
        """All agents offer up items in the marketplace to be sold."""

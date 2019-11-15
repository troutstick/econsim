import random
import marketplace

class Pop:
    """Class representing all people."""
    def __init__(self, marketplace, needs, money, inventory, goods_prices):
        """NEEDS is a dictionary: pairing up a type of material with how much they desire to buy/sell them.
        INVENTORY is a dict
        GOODS_PRICES is also a dict; adjusted with every transanction"""
        #self.size = size
        #self.ethnicity = ethnicity
        #self.religion = religion
        self.marketplace = marketplace
        self.needs = needs
        self.money = money
        self.inventory = inventory
        self.goods_prices = goods_prices
        self.buy_success = buy_success
        self.sell_success = sell_success

    def needs(self, resource, curr_price):
        """The AI function: The pop tries to fulfill its daily desires.

        resource_name = the type of resource being interacted with
        ideal_amount = how much the pop wants to buy/sell
        curr_amount = how much of this resource_name that this pop owns
        curr_price = the price of this resource_name in the pop's marketplace"""
        resource_name = resource.name
        curr_amount = self.inventory.get(resource_name)
        ideal_amount = self.needs.get(resource_name)
        expected_price = self.goods_prices.get(resource_name)
        if ideal_amount > curr_amount:
            bid = self.create_buy(resource, expected_price)
        elif ideal_amount < curr_amount:
            bid = self.create_sell(resource, expected_price)
        else:
            bid = None
        self.marketplace.add_bid(bid)

    def create_buy(self, resource, bid_price):
        """Returns an offer to buy a good at the marketplace"""
        buy_amount = amount_to_buy(self, resource)
        return Buy(self, resource, bid_price, buy_amount)

    def create_sell(self, resource, bid_price):
        """Returns an offer to sell a good at the marketplace"""
        sell_amount = amount_to_sell(self, resource)
        return Sell(self, resource, bid_price, sell_amount)

    def amount_to_buy(self, resource, curr_amount, ideal_amount):
        """Return how much of RESOURCE that the pop wants to buy.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transanctions that the pop has seen
        DEFICIT = how much of RESOURCE it would take to get to ideal_amount
        """
        deficit = ideal_amount - curr_amount
        return deficit

    def amount_to_sell(self, resource, curr_amount, ideal_amount):
        """Return how much of RESOURCE that the pop wants to sell.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transanctions that the pop has seen
        EXCESS = how much of RESOURCE is in the inventory
        """
        excess = curr_amount - ideal_amount
        return excess

    def update_price(self, resource):
        """Method to update the prices that the pop expects to encounter in its marketplace."""
        pass


        #class Lower_Class(Pop):
        """Represents people in the lower echelons of society."""

        #class Middle_Class(Pop):
        """Represents people in the middle echelons of society."""

        #class Upper_Class(Pop):
        """Represents people in the upper echelons of society."""

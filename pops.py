import random
import marketplace
import transactions

class Pop:
    """Class representing all people.
    Maybe somehow implement a way to limit a Pop's number of actions per tick;
    this could be used to represent privilege or productivity.
    """
    def __init__(self, marketplace, desires, money, inventory, goods_prices):
        """DESIRES is a dictionary: pairing up a resource with the Pop's ideal amount.
        INVENTORY is a dict containing RESOURCE objects
        GOODS_PRICES is also a dict; adjusted with every transaction"""
        #self.size = size
        #self.ethnicity = ethnicity
        #self.religion = religion
        self.marketplace = marketplace
        self.money = money
        self.inventory = inventory
        self.config_mental_state(desires, goods_prices, buy_success, sell_success)

    def config_mental_state(self, desires, goods_prices, buy_success, sell_success):
        """Function that sets up the Pop's attitudes towards things."""

        # the following are essentially part of the pop's mental state and should not be accessed by others
        self.desires = desires
        self.goods_prices = goods_prices    # expected prices for every resource according to the pop
        self.buy_success = buy_success      # history of buys; used to determine expected prices
        self.sell_success = sell_success

    #########################
    # Interfaces to interact with pop
    #########################

    def add_to_inventory(self, outside_resource, amount):
        """A function that adds/subtracts an AMOUNT of RESOURCE from the inventory."""
        resource_name = outside_resource.name
        inv_resource = self.inventory.get(resource_name)
        inv_resource += amount

    def add_cash(self, amount):
        """The Pop is given AMOUNT of cash."""
        self.money += amount

    def exchange(self, resource_name, resource_amount, cash_amount):
        """Function for an agent to exchange cash for resource."""
        self.add_to_inventory(resource_name, resource_amount)
        self.add_cash(cash_amount)

    def get_inventory(self, resource_name):
        """Looks up RESOURCE_NAME in inventory, and returns resource instance if successful."""
        return self.inventory.get(resource_name)

    def get_inventory_amount(self, resource_name):
        """Returns the amount of a resource is in the inventory."""
        return self.get_inventory(resource_name).amount

    def get_expected_price(self, resource_name):
        """Looks up the Pop's expectations for a resource's price."""
        return self.goods_prices(resource_name)

    def get_desired_amount(self, resource_name):
        """Looks up the pop's desired amount of RESOURCE."""
        return self.desires.get(resource_name)

    ###################################################

    def produce(self):
        """The pop produces/consumes material."""
        def produce_rocket():
            """An example function. Add one to rocket amount."""
            self.add_to_inventory(Rocket, 1)

        produce_rocket()

    def offer(self):
        """The pop will offer to buy/sell goods in its marketplace as it desires."""
        for resource_name in marketplace.allowed_resources:
            bid = self.pop_ai(resource_name)
            self.marketplace.add_bid(bid)

    def pop_ai(self, resource_name):
        """The AI function: The pop tries to fulfill its wishes regarding a resource.

        resource_name = the type of resource being interacted with
        ideal_amount = how much the pop wants to buy/sell
        curr_amount = how much of this resource_name that this pop owns
        curr_price = the price of this resource_name in the pop's marketplace

        Some vars unimplemented.

        Essentially creates and returns a Transaction for something.
        """
        curr_amount = self.get_inventory_amount(resource_name)
        ideal_amount = self.get_desired_amount(resource_name)
        expected_price = self.get_expected_price(resource_name)
        if ideal_amount > curr_amount:
            bid = self.create_buy(resource, expected_price)
        elif ideal_amount < curr_amount:
            bid = self.create_sell(resource, expected_price)
        else:
            bid = None
        return bid

    def create_buy(self, resource_name, bid_price):
        """Returns an offer to buy a good at the marketplace.
        Pop will buy goods that cost at most BID_PRICE, but will happily buy at lower price.
        """
        buy_amount = amount_to_buy(self, resource_name)
        return Buy(self, resource_name, bid_price, buy_amount)

        # find a way to negotiate a final price from these two
        # maybe it's the bid price of the Sell instance?
        # this makes sense

    def create_sell(self, resource_name, bid_price):
        """Returns an offer to sell a good at the marketplace.
        Pop will sell goods for at least BID_PRICE, but will happily sell at higher price.
        """
        sell_amount = amount_to_sell(self, resource_name)
        return Sell(self, resource_name, bid_price, sell_amount)

#amount_to_buy and amount_to_buy reference unimplemented variables

    def amount_to_buy(self, resource_name):
        """Return how much of RESOURCE that the pop wants to buy.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transactions that the pop has seen
        DEFICIT = how much of RESOURCE it would take to get to ideal_amount
        """
        curr_amount = self.get_inventory_amount(resource_name)
        ideal_amount = self.get_desired_amount(resource_name)
        deficit = ideal_amount - curr_amount
        return deficit

    def amount_to_sell(self, resource_name):
        """Return how much of RESOURCE that the pop wants to sell.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transactions that the pop has seen
        EXCESS = how much of RESOURCE is in the inventory
        """
        curr_amount = self.get_inventory_amount(resource_name)
        ideal_amount = self.get_desired_amount(resource_name)
        excess = curr_amount - ideal_amount
        return excess

    def update_price(self, resource_name):
        """Method to update the prices that the pop expects to encounter in its marketplace."""
        pass


        #class Lower_Class(Pop):
        """Represents people in the lower echelons of society."""

        #class Middle_Class(Pop):
        """Represents people in the middle echelons of society."""

        #class Upper_Class(Pop):
        """Represents people in the upper echelons of society.
        Maybe they have more actions or something.
        """

class Resource:
    """Class that represents all the commodities handled by the agents."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Rocket(Resource):
    """An example resource."""
    def __init__(self, amount):
        Resource.__init__(self, 'Rocket', amount)

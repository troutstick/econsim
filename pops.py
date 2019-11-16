import markets
import random
import goods

class Pop:
    """Class representing all people.
    Maybe somehow implement a way to limit a Pop's number of actions per tick;
    this could be used to represent privilege or productivity.
    """
    job = 'N/A'

    def __init__(self, name='Bob', money=0):
        """DESIRES is a dictionary: pairing up a resource with the Pop's ideal amount.
        INVENTORY is a dict containing RESOURCE objects
        GOODS_PRICES is also a dict; adjusted with every transaction"""
        #self.size = size
        #self.ethnicity = ethnicity
        #self.religion = religion
        self.name = name
        self.money = money
        self.marketplace = None
        self.inventory = {}
        self.config_pop()
        self.config_mental_state()

    def config_pop(self):
        """Default setup. WIP."""
        self.inventory = {}
        for resource in goods.implemented:
            self.inventory[resource.name] = resource(0)

    def config_mental_state(self):
        """Function that sets up the Pop's attitudes towards things.
        Essentially part of the pop's mental state and should not be accessed by others.
        """
        names = [resource.name for resource in goods.implemented]

        self.desires = {}
        self.goods_prices = {} # expected prices for every resource according to the pop
        self.buy_success = {} # history of buys; used to determine expected prices
        self.sell_success = {}

        for n in names:
            self.desires[n] = 10
            self.goods_prices[n] = 1 # expected prices for every resource according to the pop
            self.buy_success[n] = 0 # history of buys; used to determine expected prices
            self.sell_success[n] = 0

    #########################
    # Interfaces to interact with pop
    #########################

    def report(self):
        """Print various things."""
        print(f"name: {self.name}")
        print(f"job: {self.job}")
        print(f"money: {self.money}")
        print(f"marketplace: {self.marketplace}")
        print(f"inventory: {self.inventory}")
        print(f"desires: {self.desires}")
        print(f"goods_prices: {self.goods_prices}")
        print(f"buy_success: {self.buy_success}")
        print(f"sell_success: {self.sell_success}")

    def add_to_inventory(self, resource_name, amount):
        """A function that adds/subtracts an AMOUNT of RESOURCE from the inventory."""
        resource = self.inventory.get(resource_name)
        resource.amount += amount

    def add_cash(self, amount):
        """The Pop is given AMOUNT of cash."""
        self.money += amount

    def exchange(self, resource_name, resource_amount, cash_amount):
        """Function for an agent to exchange cash for resource."""
        self.add_to_inventory(resource_name, resource_amount)
        self.add_cash(cash_amount)
        self.goods_prices[resource_name] *= random.uniform(1.0, 1.25)


    def get_inventory(self, resource_name):
        """Looks up RESOURCE_NAME in inventory, and returns resource instance if successful."""
        return self.inventory.get(resource_name)

    def get_inventory_amount(self, resource_name):
        """Returns the amount of a resource is in the inventory."""
        return self.get_inventory(resource_name).amount

    def get_expected_price(self, resource_name):
        """Looks up the Pop's expectations for a resource's price."""
        return self.goods_prices.get(resource_name)

    def get_desired_amount(self, resource_name):
        """Looks up the pop's desired amount of RESOURCE."""
        return self.desires.get(resource_name)

    ###################################################

    def produce(self):
        """The pop produces/consumes material."""
        pass

    def offer(self):
        """The pop will offer to buy/sell goods in its marketplace as it desires."""
        for resource_name in self.marketplace.allowed_resources:
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
        print(resource_name, curr_amount, ideal_amount, 'hi')
        expected_price = self.get_expected_price(resource_name)
        if ideal_amount > curr_amount:
            bid = self.create_buy(resource_name, expected_price)
        elif ideal_amount < curr_amount:
            bid = self.create_sell(resource_name, expected_price)
        else:
            bid = None
        return bid

    def create_buy(self, resource_name, bid_price):
        """Returns an offer to buy a good at the marketplace.
        Pop will buy goods that cost at most BID_PRICE, but will happily buy at lower price.
        """
        desired_buy_amount = self.amount_to_buy(resource_name)
        max_buy_amount = int(self.money // bid_price)
        if max_buy_amount < 1:
            return
        buy_amount = min(desired_buy_amount, max_buy_amount)
        return markets.Buy(self, resource_name, bid_price, buy_amount)

        # find a way to negotiate a final price from these two
        # maybe it's the bid price of the Sell instance?
        # this makes sense

    def create_sell(self, resource_name, bid_price):
        """Returns an offer to sell a good at the marketplace.
        Pop will sell goods for at least BID_PRICE, but will happily sell at higher price.
        """
        sell_amount = self.amount_to_sell(resource_name)
        return markets.Sell(self, resource_name, bid_price, sell_amount)

#amount_to_buy and amount_to_buy reference unimplemented variables

    def amount_to_buy(self, resource_name):
        """Return how much of RESOURCE that the pop wants to buy.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transactions that the pop has seen
        DEFICIT = how much of RESOURCE it would take to get to ideal_amount
        """
        curr_amount = self.get_inventory_amount(resource_name)
        ideal_amount = self.get_desired_amount(resource_name)
        deficit = int(ideal_amount - curr_amount)
        return deficit

    def amount_to_sell(self, resource_name):
        """Return how much of RESOURCE that the pop wants to sell.

        MEAN = historical avg price of RESOURCE (as determined by the Resource class)
        FAVORABILITY = number between 0 and 1 determined by the transactions that the pop has seen
        EXCESS = how much of RESOURCE is in the inventory
        """
        curr_amount = self.get_inventory_amount(resource_name)
        ideal_amount = self.get_desired_amount(resource_name)
        excess = int(curr_amount - ideal_amount)
        return excess

    def update_price_belief(self, resource_name):
        """Method to update the prices that the pop expects to encounter in its marketplace."""
        clearing_price = self.marketplace.get_clearing_price(resource_name)
        expected_price = self.get_expected_price(resource_name)
        diff = clearing_price - expected_price
        self.goods_prices[resource_name] += (diff * random.random())

    def failed_buy(self, resource_name):
        """The pop adjusts expectations when faced with a failed transaction."""
        self.goods_prices[resource_name] *= random.uniform(1.0, 1.1)

    def failed_sell(self, resource_name):
        """The pop adjusts expectations when faced with a failed transaction."""
        self.goods_prices[resource_name] *= random.uniform(0.9, 1.0)

        #class Lower_Class(Pop):
        """Represents people in the lower echelons of society."""

        #class Middle_Class(Pop):
        """Represents people in the middle echelons of society."""

        #class Upper_Class(Pop):
        """Represents people in the upper echelons of society.
        Maybe they have more actions or something.
        """



class Rocketeer(Pop):
    """Makes rockets"""

    job = 'Rocketeer'

    def produce(self):
        """The pop produces/consumes material."""
        make_food(self)
        produce_rocket(self)


class Rocket_eater(Pop):
    """Consumes rockets; makes food from rockets"""

    job = 'Rocket_eater'

    def produce(self):
        """The pop produces/consumes material."""
        eat_rocket(self)

    #########################
    # Production
    #########################

def produce_rocket(agent):
    """An example function. Add one to rocket amount."""
    agent.add_to_inventory(goods.Rocket.name, 1)

def eat_rocket(agent):
    """An example function."""
    while agent.get_inventory_amount(goods.Rocket.name) > 1:
        agent.add_to_inventory(goods.Rocket.name, -1)
        salary = random.uniform(1, 10)
        #self.add_cash(salary)
        make_food(agent, 1)
        print(f'{agent.name} made one food from eating a rocket')
    else:
        agent.add_cash(1)

def make_food(agent, amount=-1):
    """Eat food"""
    agent.add_to_inventory(goods.Food.name, amount)

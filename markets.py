import pops

class Marketplace:
    """Where money is exchanged for goods and services.

    Each market has a price for each type of RESOURCE, and updates prices based on how much was bought vs sold.
    """
    def __init__(self, name, agents):
        """Agents are actors that act in the economy. Can be pops or whole nations."""
        self.name = name
        self.agents = agents
        self.clearing_price_list = {pops.Rocket.name: 4, pops.Food.name: 10} # each resource's clearing price at this market
        self.agents_config()
        self.allowed_resources_config() # creates list of all resources that can be traded here
        self.market_reset() # prepare for new trading round

    def agents_config(self):
        """Every agent is told what marketplace they operate in."""
        for agent in self.agents:
            agent.marketplace = self

    def allowed_resources_config(self):
        self.allowed_resources = [pops.Rocket.name, pops.Food.name]

    #########################
    # Interfaces to interact with marketplace
    #########################

    def report_all(self):
        for agent in self.agents:
            agent.report()

    def get_clearing_price(self, resource_name):
        """Looks up the average clearing price of a resource as of the most recent trading round."""
        return self.clearing_price_list.get(resource_name)

    #########################
    # Simulation
    #########################


    def simulate(self):
        """The invisible hand of the free market simulates the passing of a day."""
        self.perform_production()
        self.generate_offers()
        self.resolve_offers()

    def perform_production(self):
        """Various resources are produced/consumed."""
        for agent in self.agents:
            agent.produce()

    def generate_offers(self):
        """Agents offer up items in the marketplace to be sold."""
        for agent in self.agents:
            agent.offer()

    def resolve_offers(self):
        """Willing buyers and sellers perform transactions."""
        for resource_name in self.allowed_resources:
            self.resolve_for_resource(resource_name)
            self.update_clearing_price(resource_name)
            print(f'clearing prices: {self.clearing_price_list}')
            self.adjust_agents(resource_name)
            self.clearing_price_reset()
        self.market_reset()

    def resolve_for_resource(self, resource_name):
        """Resolves outstanding transactions of a specific resource type."""

        transaction_key = lambda bid: bid.bid_price

        resource_buy_list = [buy for buy in self.buy_list if buy.resource_name == resource_name]
        self.boy = resource_buy_list
        resource_sell_list = [sell for sell in self.sell_list if sell.resource_name == resource_name]
        resource_buy_list.sort(key=transaction_key, reverse=True) # buys are sorted in descending order
        resource_sell_list.sort(key=transaction_key)
        #print(resource_buy_list)
        #print('and')
        #print(resource_sell_list)
        print("len(buy): {0}\nlen(sell): {1}".format(len(resource_buy_list), len(resource_sell_list)))

        try:
            while resource_buy_list and resource_sell_list:
                perform_transaction(self, resource_buy_list.pop(0), resource_sell_list.pop(0))
            for buy in resource_buy_list:
                buy.bidder.failed_buy(resource_name)
            for sell in resource_sell_list:
                sell.bidder.failed_sell(resource_name)
            return
        except NoTransactionException:
            return

    def market_reset(self):
        """Resets stuff for a new trading round."""
        self.buy_list = []      # bids and asks
        self.sell_list = []
        self.clearing_price_reset()


    def adjust_agents(self, resource_name):
        """Agents update themselves according to what they saw took place."""
        for agent in self.agents:
            agent.update_price_belief(resource_name)


    def exchange(self, resource_name, resource_amount, cash_amount):
        """Helps to update clearing price; updates the amount of cash/material exchanged in a trading round."""
        self.material_exchanged += resource_amount
        self.money_exchanged += cash_amount

    def update_clearing_price(self, resource_name):
        """Updates the average price per unit of material sold during a trading round."""
        try:
            self.clearing_price_list[resource_name] = self.money_exchanged / self.material_exchanged
        except ZeroDivisionError:
            return

    def clearing_price_reset(self):
        """used to update clearing prices every day"""
        self.material_exchanged = 0
        self.money_exchanged = 0

    def add_bid(self, bid):
        """Adds a buy or sell bid to the marketplace."""
        if bid is None:
            return
        elif isinstance(bid, Buy):
            self.buy_list.append(bid)
        elif isinstance(bid, Sell):
            self.sell_list.append(bid)

    #########################
    # Transaction Logic
    #########################

class NoTransactionException(Exception):
    pass

class Transaction:
    """Representation of offers for buying/selling resources."""
    def __init__(self, bidder, resource_name, bid_price, amount):
        assert isinstance(amount, int), "bid amount must be int"
        self.bidder = bidder
        self.resource_name = resource_name
        self.bid_price = bid_price
        self.amount = amount

    def __repr__(self):
        if isinstance(self, Buy):
            return f"{self.bidder.name}; Buy; {self.amount} {self.resource_name}s; ${self.bid_price}"
        elif isinstance(self, Sell):
            return f"{self.bidder.name}; Sell; {self.amount} {self.resource_name}; ${self.bid_price}"

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
    buyer = buy.bidder
    seller = sell.bidder
    print(f'{buyer.name} tries to buy from {seller.name}')
    if buy.bid_price >= sell.bid_price:
        resource_amount = min(buy.amount, sell.amount)
        resource_name = buy.resource_name
        clearing_price = (buy.bid_price + sell.bid_price) / 2
        total_price = resource_amount * clearing_price

        print(f"{buyer.name} bought {resource_amount} {resource_name} from {seller.name} for only {total_price} money!")

        buyer.exchange(resource_name, resource_amount, -total_price)
        seller.exchange(resource_name, -resource_amount, total_price)
        marketplace.exchange(resource_name, resource_amount, total_price)
    else:
        print(f'{buyer.name} and {seller.name} unable to agree to a deal.')
        raise NoTransactionException('no transaction')

        #class Lower_Class(Pop):
        """Represents people in the lower echelons of society."""

        #class Middle_Class(Pop):
        """Represents people in the middle echelons of society."""

        #class Upper_Class(Pop):
        """Represents people in the upper echelons of society."""

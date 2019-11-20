import pops
import goods
from math import sqrt

class Marketplace:
    """Where money is exchanged for goods and services.

    Each market has a price for each type of RESOURCE, and updates prices based on how much was bought vs sold.
    """
    def __init__(self, name, agents):
        """Agents are actors that act in the economy. Can be pops or whole nations."""
        self.name = name
        self.agents = agents
        self.clearing_price_list = {} # each resource's clearing price at this market

        self.profit_list = {} # shows how profitable each job is
        # each key points to a list with profit values from the previous 10 rounds
        self.sorted_agents = {}

        self.rolling_avg_window = 10

        self.allowed_resources_config() # creates list of all resources that can be traded here
        self.agents_config()
        self.market_reset() # prepare for new trading round

    def __repr__(self):
        return self.name

    def agents_config(self):
        """Every agent is told what marketplace they operate in, and they are
        sorted into lists according to their jobtype.
        """
        for agent_type in pops.pop_types:
            key = agent_type.job
            self.sorted_agents[key] = []
            self.profit_list[key] = []
            for agent in self.agents:
                if isinstance(agent, agent_type):
                    self.sorted_agents[agent_type.job].append(agent)
        for agent in self.agents:
            agent.change_marketplace(self)
            self.sorted_agents[agent.job]

    def allowed_resources_config(self):
        self.allowed_resources = [r.name for r in goods.implemented]
        for resource in goods.implemented:
            self.clearing_price_list[resource.name] = 4 # each resource's clearing price at this market

    #########################
    # Interfaces to interact with marketplace
    #########################

    def list_agents(self):
        return self.sorted_agents

    def agent_population(self):
        print(f'Population: {len(self.agents)}')
        for agent_type, agent_list in self.sorted_agents.items():
            print(f'{agent_type}: {len(agent_list)}')

    def profitability(self, jobtype):
        """Returns the avg profitability of a job type over the last ROLLING_AVG_WINDOW rounds."""
        recent_profits = self.profit_list[jobtype]
        try:
            return sum(recent_profits) / len(recent_profits)
        except ZeroDivisionError:
            return float('inf')

    def most_profitable(self):
        """Returns the most profitable job at the marketplace."""

        # needs to be changed to account for poor demand elasticity

        plist = self.profit_list
        answer = max(plist, key=self.profitability)
        return answer

    def report_all(self):
        for agent in self.agents:
            print('')
            agent.report()

    def get_clearing_price(self, resource_name):
        """Looks up the average clearing price of a resource as of the most recent trading round."""
        return self.clearing_price_list.get(resource_name)

    def add_agent(self, agent):
        """Add a new agent to the marketplace."""
        self.agents.append(agent)
        self.sorted_agents[agent.job].append(agent)
        agent.change_marketplace(self)

    def remove_agent(self, agent):
        """All references to this agent in the marketplace are deleted."""
        self.agents.remove(agent)
        self.sorted_agents[agent.job].remove(agent)

    def replace_agent(self, replacer, replacee):
        """Replace one agent in the market with another."""
        self.remove_agent(replacer)
        self.add_agent(replacee)

    #########################
    # Simulation
    #########################


    def simulate(self):
        """The invisible hand of the free market simulates the passing of a day."""
        self.perform_production()
        self.generate_offers()
        self.resolve_offers()
        self.measure_profits()
        self.promote_demote()

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
        print("len(buy): {0}\nlen(sell): {1}".format(len(self.buy_list), len(self.sell_list)))
        for resource_name in self.allowed_resources:
            self.resolve_for_resource(resource_name)
            self.update_clearing_price(resource_name)
            self.adjust_agents(resource_name)
            self.clearing_price_reset()
        print(f'clearing prices: {self.clearing_price_list}')
        self.market_reset()

    def measure_profits(self):
        """Builds the rolling average list of profits; agents update their own
        profit values."""
        for agent_name, agent_list in self.sorted_agents.items():
            agents_profit = 0
            print(f"{len(agent_list)} {agent_name}")
            moving_avg_profit = self.profit_list[agent_name]
            if agent_list:
                for agent in agent_list:
                    agents_profit += agent.measure_profits()
                moving_avg_profit.append(agents_profit)
            if len(moving_avg_profit) > self.rolling_avg_window:
                moving_avg_profit.pop(0)
            elif len(agent_list) == 0 and len(moving_avg_profit) > 0:
                moving_avg_profit.pop(0)

    def promote_demote(self):
        """All unprofitable agents switch jobs.
        i.e. they are replaced with an agent with the same attributes but are a different type.
        """
        for agent in self.agents:
            agent.promote_demote()

    def resolve_for_resource(self, resource_name):
        """Resolves outstanding transactions of a specific resource type."""

        transaction_key = lambda bid: bid.bid_price

        resource_buy_list = [buy for buy in self.buy_list if buy.resource_name == resource_name]
        self.boy = resource_buy_list
        resource_sell_list = [sell for sell in self.sell_list if sell.resource_name == resource_name]
        resource_buy_list.sort(key=transaction_key, reverse=True) # buys are sorted in descending order
        resource_sell_list.sort(key=transaction_key)
        supply = len(resource_sell_list)
        demand = len(resource_buy_list)
        print(f'{resource_name} supply: {supply}')
        print(f'{resource_name} demand: {demand}')
        self.demand_supply_ratio = sqrt(demand / max(supply, 1))

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
            agent.update_price_belief(resource_name, self.demand_supply_ratio)


    def exchange(self, resource_name, resource_amount, cash_amount):
        """Helps to update clearing price; updates the amount of cash/material exchanged in a trading round."""
        self.material_exchanged += resource_amount
        self.money_exchanged += cash_amount

    def update_clearing_price(self, resource_name):
        """Updates the average price per unit of material sold during a trading round."""
        try:
            self.clearing_price_list[resource_name] = (
                self.money_exchanged / self.material_exchanged
                )
        except ZeroDivisionError:
            return

    def clearing_price_reset(self):
        """used to update clearing prices every day"""
        self.material_exchanged = 0
        self.money_exchanged = 0
        self.demand_supply_ratio = 1

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
        assert amount >= 1, 'bid amount must be positive'
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
    resource_name = buy.resource_name
    if buy.bid_price >= sell.bid_price:
        resource_amount = min(buy.amount, sell.amount)
        clearing_price = (buy.bid_price + sell.bid_price) / 2
        total_price = resource_amount * clearing_price

        print(f"{buyer.name} bought {resource_amount} {resource_name} from {seller.name} for only {clearing_price} each!")

        buyer.exchange(resource_name, resource_amount, -total_price)
        buyer.successful_buy(resource_name)
        seller.exchange(resource_name, -resource_amount, total_price)
        seller.successful_sell(resource_name)
        marketplace.exchange(resource_name, resource_amount, total_price)
    else:
        buyer.failed_buy(resource_name) # all outstanding bids also receive this
        seller.failed_sell(resource_name)
        print(f'{buyer.name} and {seller.name} unable to agree to a deal.')
        raise NoTransactionException('no transaction')

        #class Lower_Class(Pop):
        """Represents people in the lower echelons of society."""

        #class Middle_Class(Pop):
        """Represents people in the middle echelons of society."""

        #class Upper_Class(Pop):
        """Represents people in the upper echelons of society."""

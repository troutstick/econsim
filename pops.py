import markets
import random
import goods

class Pop:
    """Class representing all people.
    Maybe somehow implement a way to limit a Pop's number of actions per tick;
    this could be used to represent privilege or productivity.
    """
    job = 'N/A'

    def __init__(self, name='Bob', money=0, id='No ID'):
        """DESIRES is a dictionary: pairing up a resource with the Pop's ideal amount.
        INVENTORY is a dict containing RESOURCE objects
        GOODS_PRICES is also a dict; adjusted with every transaction"""
        #self.size = size
        #self.ethnicity = ethnicity
        #self.religion = religion
        self.id = id
        self.name = name

        self.money = money
        self.previous_money = money # used to calculate profit
        self.daily_profit = 0

        self.pennilessness = 0
        self.bankruptcy_threshold = 5
        self.bankrupt = False

        self.marketplace = None
        self.inventory = {}
        self.config_pop()
        self.config_mental_state()

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.name


    def config_pop(self):
        """Default setup. WIP."""
        self.inventory = {}
        for resource in goods.implemented:
            self.inventory[resource.name] = resource(1)

    def config_mental_state(self):
        """Function that sets up the Pop's attitudes towards things.
        Essentially part of the pop's mental state and should not be accessed by others.
        """

        self.desires = {}
        """Prices should be a dictionary with a key pointing to two numbers?
        Or some kind of object with two attributes.
        CONSIDER CREATING A CLASS FOR THIS
        """

        # WIP
        self.buy_success = {} # history of buys; used to determine expected prices
        self.sell_success = {}

        self.config_desires()

    def config_desires(self):
        names = [resource.name for resource in goods.implemented]
        for n in names:
            self.desires[n] = 10
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
        print(f"recent profit: {self.daily_profit}")
        print(f"marketplace: {self.marketplace}")
        print(f"inventory: {self.inventory}")
        print(f"desires: {self.desires}")
        for resource in goods.implemented:
            self.get_expected_price(resource.name)
        # print(f"buy_success: {self.buy_success}")
        # print(f"sell_success: {self.sell_success}")

    def add_to_inventory(self, resource_name, amount):
        """A function that adds/subtracts an AMOUNT of RESOURCE from the inventory."""
        resource = self.inventory.get(resource_name)
        resource.change_amount(amount)

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

    def get_random_price(self, resource_name):
        """Looks up the Pop's expectations for a resource's price, between
        its upper and lower bounds."""
        return self.inventory[resource_name].price.get_price()

    def get_expected_price(self, resource_name):
        print(self.inventory[resource_name].price)

    def get_desired_amount(self, resource_name):
        """Looks up the pop's desired amount of RESOURCE."""
        return self.desires.get(resource_name)

    def promote_demote(self):
        """Tries to switch jobs if it's reasonable to do so."""
        if self.money < 0:
            self.penniless()
        if self.bankrupt:
            job_name = self.marketplace.most_profitable()
            # only switch if new job is different
            if job_name != self.job:
                agent_type = [agent_type for agent_type in pop_types if agent_type.job == job_name].pop(0)
                new_instance = agent_type(self.name, self.money, self.id)
                new_instance.inventory = self.inventory
                new_instance.pennilessness = 0
                print(f'{self.name}: {self.job} -> {new_instance.job}')
                self.marketplace.replace_agent(self, new_instance)

    def penniless(self):
        """Penniless counter is increased to measure bankruptcy."""
        self.pennilessness += 1
        if self.pennilessness > self.bankruptcy_threshold:
            if not self.bankrupt:
                print(f"{self.name} goes bankrupt!")
            self.bankrupt = True

    def change_marketplace(self, marketplace):
        """Pop changes marketplace and sets up prices to match."""
        self.marketplace = marketplace
        for resource_name, resource in self.inventory.items():
            start_price = marketplace.get_clearing_price(resource_name)
            resource.price = goods.Price(resource, start_price)

    ###################################################

    def produce(self):
        """The pop produces/consumes material.
        Left blank for typeless pop.
        """
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

        Creates and returns a Transaction for something.
        """
        curr_amount = self.get_inventory_amount(resource_name)
        ideal_amount = self.get_desired_amount(resource_name)
        if ideal_amount > curr_amount:
            bid = self.create_buy(resource_name)
        elif ideal_amount < curr_amount:
            bid = self.create_sell(resource_name)
        else:
            bid = None
        return bid

    def create_buy(self, resource_name):
        """Returns an offer to buy a good at the marketplace.
        Pop will buy goods that cost at most BID_PRICE, but will happily buy at lower price.
        """
        bid_price = self.get_random_price(resource_name)
        desired_buy_amount = self.amount_to_buy(resource_name)
        max_buy_amount = int(self.money // bid_price) + 1
        buy_amount = min(desired_buy_amount, max_buy_amount)
        if buy_amount < 1:
            return
        return markets.Buy(self, resource_name, bid_price, buy_amount)

        # find a way to negotiate a final price from these two
        # maybe it's the bid price of the Sell instance?
        # this makes sense

    def create_sell(self, resource_name):
        """Returns an offer to sell a good at the marketplace.
        Pop will sell goods for at least BID_PRICE, but will happily sell at higher price.
        """
        bid_price = self.get_random_price(resource_name)
        sell_amount = self.amount_to_sell(resource_name)
        if sell_amount < 1:
            return
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

    def update_price_belief(self, resource_name, demand_supply_ratio):
        """Method to update the prices that the pop expects to encounter in its marketplace."""
        clearing_price = self.marketplace.get_clearing_price(resource_name)
        resource = self.get_inventory(resource_name)
        resource.price.shift_price_if_significant(clearing_price)

    def successful_buy(self, resource_name):
        """The Pop will try to negotiate for a lower price next time.
        WIP — the pop should be less aggressive with more experience in the market.
        """
        resource = self.get_inventory(resource_name)
        resource.price.converge()
        resource.price.decrease()

    def successful_sell(self, resource_name):
        """The Pop will become more confident in its believed price range."""
        resource = self.get_inventory(resource_name)
        resource.price.converge()
        resource.price.increase()

    def failed_buy(self, resource_name):
        """The pop lowers expectations when faced with a failed transaction.
        It will try to buy goods at a higher price in the future.
        (This means it attempts to shift price a 2nd time.)
        """
        clearing_price = self.marketplace.get_clearing_price(resource_name)
        resource = self.get_inventory(resource_name)
        resource.price.shift_price_if_significant(clearing_price)
        resource.price.diverge()

    def failed_sell(self, resource_name):
        """The pop lowers expectations when faced with a failed transaction."""
        clearing_price = self.marketplace.get_clearing_price(resource_name)
        resource = self.get_inventory(resource_name)
        resource.price.shift_price_if_significant(clearing_price)
        resource.price.diverge()

    def measure_profits(self):
        """The pop sees how much money it made (or didn't make) in the last trading round."""
        self.daily_profit = self.money - self.previous_money
        return self.daily_profit

        #class Lower_Class(Pop):
        """Represents people in the lower echelons of society."""

        #class Middle_Class(Pop):
        """Represents people in the middle echelons of society."""

        #class Upper_Class(Pop):
        """Represents people in the upper echelons of society.
        Maybe they have more actions or something.
        """

class Farmer(Pop):
    """Uses wood and tools to make food."""
    job = 'Farmer'
    def config_pop(self):
        self.inventory = {}
        self.inventory['Food'] = goods.Food(1)
        self.inventory['Tool'] = goods.Tool(1)
        self.inventory['Wood'] = goods.Wood(4)
        self.inventory['Iron'] = goods.Iron(0)

    def config_desires(self):
        self.desires['Food'] = 0
        self.desires['Tool'] = 2
        self.desires['Wood'] = 5
        self.desires['Iron'] = 0

    def produce(self):
        eat_food(self)
        if not self.marketplace.famine:
            tool_amount = self.get_inventory_amount('Tool')
            wood_amount = self.get_inventory_amount('Wood')
            if wood_amount and tool_amount:
                self.add_to_inventory('Food', 4)
                self.add_to_inventory('Wood', -1)
                if random.random() < 0.1:
                    self.add_to_inventory('Tool', -1)
            elif wood_amount:
                self.add_to_inventory('Food', 2)
                self.add_to_inventory('Wood', -1)

class Miner(Pop):
    """Mines for iron."""
    job = 'Miner'
    def config_pop(self):
        self.inventory = {}
        self.inventory['Food'] = goods.Food(5)
        self.inventory['Tool'] = goods.Tool(1)
        self.inventory['Wood'] = goods.Wood(0)
        self.inventory['Iron'] = goods.Iron(0)
    def config_desires(self):
        self.desires['Food'] = 10
        self.desires['Tool'] = 2
        self.desires['Wood'] = 5
        self.desires['Iron'] = 0

    def produce(self):
        eat_food(self)
        tool_amount = self.get_inventory_amount('Tool')
        if not self.marketplace.earthquake:
            if tool_amount:
                self.add_to_inventory('Iron', 4)
                if random.random() < 0.1:
                    self.add_to_inventory('Tool', -1)
            else:
                self.add_to_inventory('Iron', 2)

class Woodcutter(Pop):
    job = 'Woodcutter'
    def config_pop(self):
        self.inventory = {}
        self.inventory['Food'] = goods.Food(5)
        self.inventory['Tool'] = goods.Tool(1)
        self.inventory['Wood'] = goods.Wood(0)
        self.inventory['Iron'] = goods.Iron(0)

    def config_desires(self):
        self.desires['Food'] = 10
        self.desires['Tool'] = 2
        self.desires['Wood'] = 0
        self.desires['Iron'] = 0

    def produce(self):
        eat_food(self)
        tool_amount = self.get_inventory_amount('Tool')
        if tool_amount and not self.marketplace.wildfire:
            self.add_to_inventory('Wood', 1)
        else:
            return

class Blacksmith(Pop):
    job = 'Blacksmith'

    def config_pop(self):
        self.inventory = {}
        self.inventory['Food'] = goods.Food(5)
        self.inventory['Tool'] = goods.Tool(0)
        self.inventory['Wood'] = goods.Wood(0)
        self.inventory['Iron'] = goods.Iron(5)

    def config_desires(self):
        self.desires['Food'] = 10
        self.desires['Tool'] = 0
        self.desires['Wood'] = 0
        self.desires['Iron'] = 10

    def produce(self):
        def smith_tools():
            """An example function."""
            k = 0
            while self.get_inventory_amount('Iron') > 1:
                self.add_to_inventory('Iron', -1)
                self.add_to_inventory('Tool', 1)
                k += 1
            if k > 0:
                print(f'{self.name} made {k} Tool')
        eat_food(self)
        smith_tools()

class Rocketeer(Pop):
    """Makes rockets"""
    job = 'Rocketeer'
    def produce_rocket(self):
        """An example function. Add one to rocket amount."""
        self.add_to_inventory('Rocket', 1)

    def produce(self):
        """The pop produces/consumes material."""
        eat_food(self)
        self.produce_rocket()

class Rocket_eater(Pop):
    """Consumes rockets; makes food from rockets"""
    job = 'Rocket_eater'
    def eat_rocket(self):
        """An example function."""
        k = 0
        while self.get_inventory_amount('Rocket') > 1:
            self.add_to_inventory('Rocket', -1)
            self.add_to_inventory('Food', 2)
            k += 1
        if k > 0:
            print(f'{self.name} ate {k} Rocket and made {k} Food')

    def produce(self):
        """The pop produces/consumes material."""
        self.eat_rocket()
        eat_food(self)

    #########################
    # Production
    #########################

def eat_food(agent):
    """Daily food need simulated."""
    try:
        agent.add_to_inventory('Food', -1)
    except goods.ResourceException:
        agent.add_cash(-2)

# shows all jobs
pop_types = [Farmer, Miner, Woodcutter, Blacksmith]

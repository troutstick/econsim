import markets
import random

#########################
# Resources
#########################

class Resource:
    """Class that represents all the commodities handled by the agents."""
    name = 'GENERIC_RESOURCE'
    def __init__(self, amount):
        assert isinstance(amount, int), "Can only have whole numbers of resources"
        assert amount >= 0, 'Resources must be nonnegative'
        self.amount = amount
        self.price = None

    def __repr__(self):
        return f'{self.amount} {self.name}'

    #########################
    # Interfacing
    #########################

    def change_amount(self, amount):
        """Change the amount of RESOURCE by an integer AMOUNT."""
        assert isinstance(amount, int), "Can only have whole numbers of resources"
        if -amount > self.amount:
            raise ResourceException("Resource amount can't go below 0")
        self.amount += amount

    #########################
    # Resource Types
    #########################

class Rocket(Resource):
    """An example resource."""
    name = 'Rocket'

class Food(Resource):
    name = 'Food'

class Tool(Resource):
    name = 'Tool'

class Wood(Resource):
    name = 'Wood'

class Iron(Resource):
    name = 'Iron'

class ResourceException(Exception):
    pass

implemented = [Food, Tool, Wood, Iron]

#########################
# Prices
#########################

class Price:
    """Models the expected prices of various resources by a Pop.
    Maybe it should be an attribute of a resource? Yes."""

    min_price = 1.0
    convergence_rate = 0.05
    significance = 0.25 # price diff is significant if more than 25 percent

    def __init__(self, resource, start_price):
        self.resource = resource
        assert start_price > 0, 'price must be positive'
        self.upper = start_price * 1.5 # the two price bounds
        self.lower = start_price * 0.5
        self.keep_min_price()

    def __repr__(self):
        return f"{self.resource}: ${self.lower}-${self.upper}"

    #########################
    # Interfacing
    #########################

    def keep_min_price(self):
        """Prevents price from dipping below the min."""
        if self.upper < self.min_price:
            self.upper = self.min_price
        if self.lower < self.min_price:
            self.lower = self.min_price
        if self.upper < self.lower:
            self.upper, self.lower = self.lower, self.upper

    def get_price(self):
        """Return a number between the upper and lower bounds."""
        return random.uniform(self.lower, self.upper)

    def get_average(self):
        return (self.upper + self.lower) / 2

    def shift_price_if_significant(self, target_price):
        """Will shift price only if difference is significant."""
        curr_price = self.get_average()
        percent_diff = (2 * abs(curr_price - target_price)) / (curr_price + target_price)
        if self.significance < percent_diff:
            self.shift_price(curr_price, target_price)

    def shift_price(self, curr_price, target_price):
        """Price bounds are shifted towards the target_price."""
        delta = target_price - curr_price
        self.upper += delta / 2
        self.lower += delta / 2
        self.keep_min_price()

    def converge(self):
        """Price bounds shift towards mean"""
        curr_price = self.get_average()
        shift = curr_price * self.convergence_rate
        self.upper -= shift
        self.lower += shift
        self.keep_min_price()

    def diverge(self):
        """Price bounds shift away from mean"""
        curr_price = self.get_average()
        shift = curr_price * self.convergence_rate
        self.upper += shift
        self.lower -= shift
        self.keep_min_price()

    def increase(self):
        self.upper *= 1 + self.convergence_rate
        self.lower *= 1 + self.convergence_rate

    def decrease(self):
        self.upper *= 1 - self.convergence_rate
        self.lower *= 1 - self.convergence_rate

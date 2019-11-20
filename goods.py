import markets

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
        if -amount >= self.amount:
            raise ResourceException("Resource amount can't go below 0")
        self.amount += amount

class Rocket(Resource):
    """An example resource."""
    name = 'Rocket'
    def __init__(self, amount):
        Resource.__init__(self, amount)

class Food(Resource):
    name = 'Food'
    def __init__(self, amount):
        Resource.__init__(self, amount)

class ResourceException(Exception):
    pass

    #########################
    # Logic for changing one type of resource into another
    #########################

implemented = [Rocket, Food]

class Price:
    """Models the expected prices of various resources by a Pop.
    Maybe it should be an attribute of a resource? Yes."""

    min_price = 0.01
    convergence_rate = 0.05
    significance = 0.25 # price diff is significant if more than 25 percent

    def __init__(self, resource, start_price):
        self.resource = resource
        assert start_price > 0, 'price must be positive'
        self.upper = start_price * 1.5 # the two price bounds
        self.lower = start_price * 0.5
        self.keep_min_price()

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
        return random.uniform(self.lower, self.higher)

    def get_average(self):
        return (self.upper + self.lower) / 2

    def shift_price_if_significant(self, target_price):
        """Will shift price only if difference is significant."""
        curr_price = get_average(self)
        percent_diff = (2 * abs(curr_price - target_price)) / (curr_price + target_price)
        if significance < percent_diff:
            shift_price(self, curr_price, target_price)

    def shift_price(self, curr_price, target_price):
        """Price bounds are shifted towards the target_price."""
        delta = target_price - curr_price
        self.upper += delta / 2
        self.lower += delta / 2
        self.keep_min_price()

    def converge(self):
        """Price bounds shift towards mean"""
        curr_price = get_average(self)
        shift = curr_price * self.convergence_rate
        self.upper -= shift
        self.lower += shift
        self.keep_min_price()

    def diverge(self):
        """Price bounds shift away from mean"""
        curr_price = get_average(self)
        shift = curr_price * self.convergence_rate
        self.upper += shift
        self.lower -= shift
        keep_min_price()

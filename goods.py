
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

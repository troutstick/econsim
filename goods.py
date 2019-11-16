
    #########################
    # Resources
    #########################

class Resource:
    """Class that represents all the commodities handled by the agents."""
    name = 'GENERIC_RESOURCE'
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'{self.amount} {self.name}'

class Rocket(Resource):
    """An example resource."""
    name = 'Rocket'
    def __init__(self, amount):
        Resource.__init__(self, amount)

class Food(Resource):
    name = 'Food'
    def __init__(self, amount):
        Resource.__init__(self, amount)

implemented = [Rocket, Food]

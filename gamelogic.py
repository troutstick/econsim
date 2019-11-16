import pops
import transactions
import marketplace

class World:
    """The world in which the simulation takes place."""
    def __init__(self):
        self.time = 0
        self.agents = []
        self.marketplaces = []
        self.config_agents()
        self.config_marketplaces()

    def config_agents(self):
        """Set up the agents."""
        pass

    def config_marketplaces(self):
        """Set up the marketplaces."""
        pass

    def simulate(self, time):
        """Run the simulation forward one timestep."""
        while self.time < time:
            for marketplace in self.marketplaces:
                marketplace.simulate_market()
            self.time += 1

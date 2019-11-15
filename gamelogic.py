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
        self.config_marketplace()

    def config_agents(self):
        """Set up the agents."""
        pass

    def config_marketplace(self):
        """Set up the marketplaces."""
        pass

    def simulate(self):
        """Run the simulation forward one timestep."""
        for marketplace in self.marketplaces:
            marketplace.simulate_market()
        self.time += 1

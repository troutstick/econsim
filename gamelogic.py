import pops
import markets

class World:
    """The world in which the simulation takes place."""
    def __init__(self, agents=[], marketplaces = [], ):
        self.time = 0
        self.agents = agents
        self.marketplaces = marketplaces
        self.config_agents()
        self.config_marketplaces()

    def config_agents(self):
        """Set up the agents."""
        pass

    def config_marketplaces(self):
        """Set up the marketplaces."""
        pass

    def simulate(self, time=1):
        """Run the simulation forward one timestep."""
        for _ in list(range(time)):
            print('')
            print(f"Worldtime: {self.time}")
            for marketplace in self.marketplaces:
                marketplace.simulate()
            self.time += 1

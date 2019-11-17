#########################
# Set up a sample world!
#########################

import gamelogic
import markets
import pops
import goods
import random
import name_gen
names = name_gen.name_generator()
ids = name_gen.id_generator()

rocketeer = pops.Rocketeer
rocket_eater = pops.Rocket_eater
r = random.randint

#bob = rocketeer('Bob', 100)

rocketeers = [rocketeer(next(names), r(0, 1000), next(ids)) for _ in range(20)]
rocket_eaters = [rocket_eater(next(names), r(0, 1000), next(ids)) for _ in range(20)]


agents = rocketeers + rocket_eaters
market = markets.Marketplace('London', agents)
earth = gamelogic.World([market])
s = earth.simulate
r = market.report_all
p = market.agent_population
print("Use s(time) to simulate, and r() to get reports from agents in the market")

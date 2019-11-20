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
farmer = pops.Farmer
miner = pops.Miner
woodcutter = pops.Woodcutter
blacksmith = pops.Blacksmith
r = random.randint

#bob = rocketeer('Bob', 100)

farmers = [farmer(next(names), r(0, 1000), next(ids)) for _ in range(20)]
miners = [miner(next(names), r(0, 1000), next(ids)) for _ in range(20)]
woodcutters = [woodcutter(next(names), r(0, 1000), next(ids)) for _ in range(5)]
smiths = [blacksmith(next(names), r(0, 1000), next(ids)) for _ in range(2)]


agents = farmers + miners + woodcutters + smiths
market = markets.Marketplace('London', agents)
earth = gamelogic.World([market])
s = earth.simulate
r = market.report_all
p = market.agent_population
print("Use s(time) to simulate, and r() to get reports from agents in the market")

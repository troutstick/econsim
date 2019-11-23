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

farmers = [farmer(next(names), r(0, 100), next(ids)) for _ in range(200)]
miners = [miner(next(names), r(0, 100), next(ids)) for _ in range(100)]
woodcutters = [woodcutter(next(names), r(0, 100), next(ids)) for _ in range(150)]
smiths = [blacksmith(next(names), r(0, 100), next(ids)) for _ in range(20)]


agents = farmers + miners + woodcutters + smiths
market = markets.Marketplace('London', agents)
earth = gamelogic.World([market])
s = earth.simulate
r = market.report_all
p = market.agent_population
most = market.most_profitable

famine = market.famine_config
earthquake = market.earthquake_config
wildfire = market.wildfire_config

print("Use s(time) to simulate.")
print("Use r() to get reports from agents in the market")
print("Use p() to get market population")
print("Use most() to get most profitable job")
print("Set natural disasters with famine(), earthquake(), or wildfire()")

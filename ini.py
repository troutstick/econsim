#########################
# Set up a sample world!
#########################

import gamelogic
import markets
import pops

maker = pops.Rocketeer
eater = pops.Rocket_eater

bob = maker('Bob', 1)
harold = maker('Harold', 241)
mark = eater('Mark')
richard = eater('Richard')
ken = maker('Ken', 12)

bob.report()

agents = [bob, harold, mark, richard, ken]
market = markets.Marketplace('London', agents)
print(f"rocket clearing price: {market.get_clearing_price('Rocket')}")
market.simulate()
earth = gamelogic.World([agents], [market])
earth.simulate(10)
s = earth.simulate
r = market.report_all

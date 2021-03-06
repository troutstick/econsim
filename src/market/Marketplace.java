package market;

import java.util.ArrayList;
import java.util.List;

public class Marketplace {

    final String NAME;

    /** The number of rounds used to calculate rolling avgs for this market's stats. */
    final int ROLLING_AVG_WINDOW = 10;

    /** What kind of currency is used to buy/sell goods at this marketplace. */
    private Money _money;

    /** The Pops that are in this marketplace. */
    List<Pop> _agents;

    Marketplace(String name, List<Pop> agents) {
        NAME = name;
        _agents = new ArrayList<>();
        _agents.addAll(agents);
    }

    /** How many Pops live here. */
    int population() {
        return _agents.size();
    }

    /** Check what kind of currency is traded at this marketplace. */
    Money money() { return _money; }
}

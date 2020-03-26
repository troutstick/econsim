package market;

import java.util.HashMap;
import java.util.Map;

/** Things that a Pop owns, whether they're objects or currencies. */
class Inventory {



    /** The resources contained by the inventory. */
    private Map<Resource, Integer> _resources;

    Inventory() {
        _resources = new HashMap<>();
    }

    /** Show how much of RESOURCE this inventory contains. */
    int peek(Resource resource) {
        return _resources.getOrDefault(resource, 0);
    }

    void addResource(Resource resource, int amount) {
        _resources.put(resource, amount + peek(resource));
    }
}
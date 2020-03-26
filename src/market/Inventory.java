package market;

import java.util.HashMap;
import java.util.Map;

/** Things that a Pop owns, whether they're objects or currencies. */
class Inventory implements ResourceHolder<Resource, Integer> {

    /** The resources contained by the inventory. */
    private Map<Resource, Integer> _resources;

    Inventory() {
        _resources = new HashMap<>();
    }

    /** Show how much of RESOURCE this inventory contains. */
    @Override
    public Integer peek(Resource resource) {
        return _resources.getOrDefault(resource, 0);
    }

    /** Add AMOUNT of RESOURCE to inventory, as long as it is not left with negative amount. */
    @Override
    public boolean addResource(Resource resource, Integer amount) {
        int newAmount = amount + peek(resource);
        if (newAmount >= 0) {
            _resources.put(resource, newAmount);
            return true;
        } else {
            return false;
        }
    }
}
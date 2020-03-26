package market;

import java.util.HashMap;
import java.util.Map;

/** A class representing an agent in the market.
 *  Can buy and sell things. What a guy.
 *  */
public class Pop {
    private final String _NAME;
    private double _money;

    /* The market this pop trades in. */
    private Marketplace _marketplace;

    /* Times to warn pop before it's bankrupt. */
    private int _bankruptcyThreshold;
    private boolean _isBankrupt;

    private Inventory _inventory;

    public Pop(String name, int id, double money) {
        _NAME = name;
        _money = money;
        _marketplace = null;
        _isBankrupt = false;
        _bankruptcyThreshold = 5;
        _inventory = new Inventory();
    }

    /** Things that a Pop owns, whether they're objects or currencies. */
    class Inventory {

        /** A wallet contains money. */
        private Map<Money, Double> _wallet;

        /** The resources contained by the inventory. */
        private Map<Resource, Integer> _resources;

        private Inventory() {
            _wallet = new HashMap<>();
            _resources = new HashMap<>();
        }

        /** Show how much of RESOURCE this inventory contains. */
        int peek(Resource resource) {
            return _resources.getOrDefault(resource, 0);
        }

        void addResource(Resource resource, int amount) {
            _resources.get(resource);
            _resources.put(resource, )
        }
    }
}

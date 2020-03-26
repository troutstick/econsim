package market;

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

    public Pop(String name) {
        _NAME = name;
        _marketplace = null;
        _isBankrupt = false; _bankruptcyThreshold = 5;
        _inventory = new Inventory();
    }
}

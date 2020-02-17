package market;

/** A class representing an agent in the market.
 *  Can buy and sell things. What a guy.
 *  */
public class Pop {
    private String _name, _id;
    private double _money;
    private Marketplace _marketplace;
    private boolean _isBankrupt;

    /** Times to warn pop before it's bankrupt. */
    private int _bankruptcyThreshold;

    public Pop(String name, String id, double money) {
        _name = name;
        _id = id;
        _money = money;
        _isBankrupt = false;
        _marketplace = null;
        _bankruptcyThreshold = 5;
    }
}

package market;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/** A class representing an agent in the market.
 *  Can buy and sell things. What a guy.
 *  */
public class Pop {
    private final String _NAME;

    /* The market this pop trades in. */
    private Marketplace _marketplace;

    /* Times to warn pop before it's bankrupt. */
    private int _bankruptcyThreshold;
    private boolean _isBankrupt;

    private Inventory _inventory;
    private Wallet _wallet;

    /* This Pop's trading history. */
    private List<Transaction> _transactions;
    private List<CurrencyTrade> _fxExchanges;

    /* Shows how much the pop wants each resource. */
    private Map<Resource, Integer> _desires;

    public Pop(String name) {
        _NAME = name;
        _marketplace = null;
        _isBankrupt = false; _bankruptcyThreshold = 5;
        _inventory = new Inventory();
        _wallet = new Wallet();
        _transactions = new ArrayList<>();
        _fxExchanges = new ArrayList<>();
    }

    /** Complete the contents of transaction T. */
    void exchange(Transaction t) {
        int resourceAmt = t.amountBought();
        double cashAmt = t.moneyAmount();
        if (t._buyer.equals(this)) {
            cashAmt *= -1;
        } else if (t._seller.equals(this)) {
            resourceAmt *= -1;
        } else {
            throw new IllegalArgumentException("transaction doesn't involve pop");
        }
        _inventory.add(t.resource(), resourceAmt);
        _wallet.add(t.moneyType(), cashAmt);
    }
}

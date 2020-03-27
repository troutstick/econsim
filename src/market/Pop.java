package market;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import static market.Resource.*;

/** A class representing an agent in the market.
 *  Can buy and sell things. What a guy.
 *  */
abstract class Pop {
    private final String _NAME;

    /*  The market this pop trades in. */
    private Marketplace _marketplace;

    /*  Times to warn pop before it's bankrupt. */
    private int _bankruptcyThreshold;
    private boolean _isBankrupt;

    private Inventory _inventory;
    private Wallet _wallet;

    /*  This Pop's trading history.
    *   Maybe should be a queue? Should contain only transactions from recent trading rounds.
    *   */
    private List<Transaction> _transactions;
    private List<CurrencyTrade> _fxExchanges;

    /*  Shows how much the pop wants each resource.
    *   Each Pop type has their own desired amount of resources.
    *   */
    private static Map<Resource, Integer> _desires;

    Pop(String name) {
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
        if (!t.transactionDone()) {
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

    static void changeDesire(Resource r, int desire) {
        _desires.put(r, desire);
    }

    /** Return how many of R this Pop wants in its inventory. */
    private int desiredAmount(Resource r) {
        return _desires.getOrDefault(r, 0);
    }

    /** The pop will try to buy and sell goods at its marketplace. */
    void produceOffers() {
        for (Resource r : Resource.values()) {
            // TODO
        }
    }
}

class Farmer extends Pop {

    static {
        Map<Resource, Integer> _desires = new HashMap<>();
        _desires.put(Grain, 10);
        _desires.put(Wood, 10);
    }

    Farmer(String name) {
        super(name);
    }
}
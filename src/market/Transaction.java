package market;

/** Represents an exchange of a resource for money. */
public class Transaction {
    private final Resource _r;
    private final int _rAmount;
    private final Money _m;
    private final double _mAmount;
    final Pop _buyer, _seller;
    private boolean _transactionDone;

    /** Trade RAMOUNT of R for MAMOUNT of M.
     *  Buyer gets resource, seller gets money. */
    Transaction(Pop buyer, Resource r, int rAmount, Pop seller, Money m, double mAmount) {
        _r = r;
        _rAmount = rAmount;
        _m = m;
        _mAmount = mAmount;
        _buyer = buyer;
        _seller = seller;
        _transactionDone = false;
    }

    /** Get the resource that was traded in the transaction. */
    Resource resource() {
        return _r;
    }

    /** Get the type of currency in the transaction. */
    Money moneyType() {
        return _m;
    }

    /** How much of the resource was bought. */
    int amountBought() {
        return _rAmount;
    }

    /** How much money was used to buy in the transaction. */
    double moneyAmount() {
        return _mAmount;
    }

    boolean transactionDone() {
        return _transactionDone;
    }

    void completeTransaction() {
        _transactionDone = true;
    }
}

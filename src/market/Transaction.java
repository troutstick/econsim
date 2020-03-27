package market;

/** Represents an exchange of a resource for money. */
public class Transaction {
    final Resource _r;
    final int _rAmount;
    final Money _m;
    final double _mAmount;

    /** Trade RAMOUNT of R for MAMOUNT of M. */
    Transaction(Resource r, int rAmount, Money m, double mAmount) {
        _r = r;
        _rAmount = rAmount;
        _m = m;
        _mAmount = mAmount;
    }
}

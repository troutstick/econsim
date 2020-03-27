package market;

/** Represents an FX trade between two Pops. */
public class CurrencyTrade {
    final Money MONEY1, MONEY2;
    final double AMOUNT1, AMOUNT2;
    final Pop TRADER1, TRADER2;

    /** TRADER1 gets AMOUNT1 of M1, while TRADER2 gets AMOUNT2 of M2. */
    CurrencyTrade(Pop trader1, Money m1, double amount1, Pop trader2, Money m2, double amount2) {
        if (trader1.equals(trader2) || m1 == m2 || amount1 < 0 || amount2 < 0) {
            throw new IllegalArgumentException("bad currency trade");
        }
        TRADER1 = trader1;
        TRADER2 = trader2;
        AMOUNT1 = amount1;
        AMOUNT2 = amount2;
        MONEY1 = m1;
        MONEY2 = m2;
    }
}

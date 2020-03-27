package market;

abstract class Offer {
    private final Resource R;
    private final int R_AMOUNT;
    private final Money M;
    private final double PRICE_PER_UNIT;
    private final Pop POP;

    /** A bid for R_AMOUNT of R at PRICE_PER_UNIT of M. */
    Offer(Pop pop, Resource r, int rAmount, Money m, double pricePerUnit) {
        POP = pop;
        R = r;
        R_AMOUNT = rAmount;
        M = m;
        PRICE_PER_UNIT = pricePerUnit;
    }

    Pop pop() {
        return POP;
    }

    Resource resource() {
        return R;
    }

    int resourceAmount() {
        return R_AMOUNT;
    }

    Money money() {
        return M;
    }

    double pricePerUnit() {
        return PRICE_PER_UNIT;
    }

}

class Buy extends Offer {

    /** A bid to buy R_AMOUNT of R at PRICE_PER_UNIT of M. */
    Buy(Pop pop, Resource r, int rAmount, Money m, double pricePerUnit) {
        super(pop, r, rAmount, m, pricePerUnit);
    }

}

class Sell extends Offer {

    /** A bid to sell R_AMOUNT of R at PRICE_PER_UNIT of M. */
    Sell(Pop pop, Resource r, int rAmount, Money m, double pricePerUnit) {
        super(pop, r, rAmount, m, pricePerUnit);
    }
}
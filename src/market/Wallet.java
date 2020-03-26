package market;

import java.util.HashMap;
import java.util.Map;

public class Wallet implements ResourceHolder<Money> {

    /** A wallet contains money. */
    private Map<Money, Double> _wallet;

    Wallet() {
        _wallet = new HashMap<>();
    }

    /** Show how much of MONEY this wallet contains. */
    @Override
    public Double peek(Money money) {
        return _wallet.getOrDefault(money, 0.0);
    }

    @Override
    public void addResource(Money money, Double amount) {

    }
}

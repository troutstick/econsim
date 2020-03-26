package market;

import java.util.HashMap;
import java.util.Map;

public class Wallet implements ResourceHolder<Money, Double> {

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

    /** Add AMOUNT of MONEY to the wallet. */
    @Override
    public void addResource(Money money, Double amount) {
        _wallet.put(money, amount + peek(money));
    }
}

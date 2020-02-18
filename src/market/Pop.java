package market;

/** A class representing an agent in the market.
 *  Can buy and sell things. What a guy.
 *  */
public class Pop {
    private String _name;
    private int _id;
    private double _money;
    private Marketplace _marketplace;
    private boolean _isBankrupt;

    /** Times to warn pop before it's bankrupt. */
    private int _bankruptcyThreshold;

    private Inventory _inventory;

    public Pop(String name, int id, double money) {
        _name = name;
        _id = id;
        _money = money;
        _isBankrupt = false;
        _marketplace = null;
        _bankruptcyThreshold = 5;
    }

    public class Inventory {
        private Inventory() {

        }

        public Inventory getInventory(Pop pop) {
            if (pop._inventory == null) {
                pop._inventory = new Inventory();
            }
            return pop._inventory;
        }

        public void addGoods() {

        }
    }
}

package market;

/** Represents resources that exist in inventories. */
public abstract class Resource {
    private int _quantity;

    private Resource(int quantity){
        _quantity = quantity;
    }

    public int getQuantity() {
        return _quantity;
    }

    public void add(int amount) {
        _quantity += amount;
    }
}

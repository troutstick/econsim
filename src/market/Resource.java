package market;

<<<<<<< HEAD
public class Resource {
=======
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
>>>>>>> e83ac6c81d0637a8b9a1ff9a087a342b60df35c2
}

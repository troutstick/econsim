package market;

import java.util.regex.Pattern;

/** Represents resources that exist in inventories. */
enum Resource {

    /** Some resource types to play around with. */
    Wood,
    Coal, Charcoal, Oil,
    Food, GourmetFood,
    Chocolate,
    Iron, Gold, Silver, Copper, Tin,
    Spice, Meat, Grain,
    Diamond, Ruby, Jade, Sapphire,
    Cotton, Silk, Tea, Coffee, Cocoa, Tobacco, Sugar,
    Lithium,
    Uranium;

    /** Tells if this is edible. */
    boolean isEdible() {
        switch (this) {
            case Food:
            case GourmetFood:
            case Chocolate:
            case Meat:
            case Grain:
            case Sugar:
                return true;
            default:
                return false;
        }
    }

    /** Tells if you can make clothes with this. */
    boolean isFabric() {
        switch (this) {
            case Cotton:
            case Silk:
                return true;
            default:
                return false;
        }

    }

    /** Tells if this can be grown on a farm. */
    boolean isGrowable() {
        switch (this) {
            case Grain:
            case Spice:
            case Cotton:
            case Tea:
            case Coffee:
            case Cocoa:
            case Tobacco:
            case Sugar:
                return true;
            default:
                return false;
        }
    }

    /** Tells if this is raw food. */
    boolean isRawFood() {
        switch (this) {
            case Meat:
            case Grain:
            case Sugar:
                return true;
            default:
                return false;
        }
    }

    /** Tells if this can be used for fuel. */
    boolean isFuel() {
        switch (this) {
            case Wood:
            case Oil:
            case Coal:
            case Charcoal:
                return true;
            default:
                return false;
        }
    }

    /** Tells if this is a metal. */
    boolean isMetal() {
        switch (this) {
            case Iron:
            case Gold:
            case Silver:
            case Copper:
            case Tin:
            case Lithium:
            case Uranium:
                return true;
            default:
                return false;
        }
    }

    /** Tells if this is a gemstone. */
    boolean isGemstone() {
        switch (this) {
            case Diamond:
            case Ruby:
            case Jade:
            case Sapphire:
                return true;
            default:
                return false;
        }
    }

}
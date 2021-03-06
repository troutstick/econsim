package market;

/** A thing that holds resources. */
interface ResourceHolder <R, N extends Number> {

    /** Check inside the holder for how much RESOURCE it contains. */
    Number peek(R resource);

    /** Add AMOUNT to the value of RESOURCE. Returns true if operation is success. */
    boolean add(R resource, N amount);


}

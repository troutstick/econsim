package market;

/** A thing that holds resources. */
interface ResourceHolder <R> {

    /** Check inside the holder for how much RESOURCE it contains. */
    Number peek(R resource);

    /** Add AMOUNT to the value of RESOURCE. */
    void addResource(R resource, Number amount);


}

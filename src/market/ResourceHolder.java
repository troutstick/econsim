package market;

/** A thing that holds resources. */
interface ResourceHolder <Resource, Amount> {

    /** Check inside the holder for how much RESOURCE it contains. */
    Amount peek(Resource resource);

    /** Add AMOUNT to the value of RESOURCE. */
    void addResource(Resource resource, Amount amount);


}

import java.math.BigInteger;

/**
 * Created with IntelliJ IDEA.
 * User: theraccoun
 * Date: 11/5/12
 * Time: 1:25 AM
 * To change this template use File | Settings | File Templates.
 */
public class Main {

    public static void main(String[] args)
    {
        BigInteger n = new BigInteger("121932632103337941464563328643500519");
        PollardRho.factor(n);
    }
}

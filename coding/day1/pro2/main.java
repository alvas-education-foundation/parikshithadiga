package pro2;
public class main
{
    public static void main(String[] args) 
    {
        printer p = new printer();
         
        odd o = new odd(20,p);
         
        o.setName("pong");
         
        even e = new even(20,p);
         
        e.setName("ping");
         
        o.start();
         
        e.start();
    }
}

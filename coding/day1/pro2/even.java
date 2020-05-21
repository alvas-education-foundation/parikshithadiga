
package pro2;
class even extends Thread
{
int limit;
printer p;
public even(int limit, printer p)
{
this.limit = limit;
this.p = p;
}
@Override
public void run() 
{
int evenNumber = 2;           
while (evenNumber <= limit)
{
p.printEven(evenNumber);         
evenNumber = evenNumber + 2;           
}
}
}

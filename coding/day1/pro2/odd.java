package pro2;
class odd extends Thread
{
int limit; 
printer p;
public odd(int limit, printer p)
{
this.limit = limit;
this.p = p;
}
@Override
public void run() 
{
int oddNumber = 1;        
while (oddNumber <= limit)
{
p.printOdd(oddNumber);       
oddNumber = oddNumber + 2;         
}
}
}

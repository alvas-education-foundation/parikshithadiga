import java.util.*;  
class armstrong
{
 public static void main(String []a)
 {
 Scanner s =new Scanner(System.in);
 System.out.println("enter the number");
 int num=s.nextInt();
 System.out.println(num);
 int t=num;
 int n,c,sum=0;
 while(t!=0)
 {
 	n=t%10;
 	t=t/10;
 	c=n*n*n;
 	sum+=c;
		
 }
 if(num==sum)
 {
  System.out.println("number is armstrong");
  
 }
 else
 {
 System.out.println("number isnt armstrong");
 }
}
}

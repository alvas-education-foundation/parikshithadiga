name="micheal"
password="e3$wt89x"
c=0
while(c!=3):
    c+=1
    testname=str(input("enter username:"))
    testpass=str(input("enter password:"))
    if((testname==name)and(password==testpass)):
	print("you have successfully login")
	break
    else:
        print("invalid username and password")
if(c==3):
    print("account locked")
	


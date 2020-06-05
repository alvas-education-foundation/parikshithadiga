l=[]
c=0
n=int(input())
for i in range(0,n):
    l.append(int(input()))
print(l)
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if(l[i]>l[j]):
            print(l[i],l[j])
            c=c+1
print(c)


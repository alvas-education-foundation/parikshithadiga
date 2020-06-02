l=[]
ld=[]
n=int(input())
for i in range(0,n):
    l.append(int(input()))
print(l)
i=0
while i<len(l):
    print(i)
    ld.append(max(l[i:]))
    i=l.index(max(l[i:]))
    i=i+1
print(ld)


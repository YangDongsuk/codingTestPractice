n,m=map(int,input().split())
lst=[]
d=[10001]*(m+1)
for i in range(n):
    lst.append(int(input()))
d[0]=0
for i in lst:
    for j in range(i,m+1):
        d[j]=min(d[j-i]+1,d[j])
if d[m]==10001:
    print(-1)
else:
    print(d[m])
    


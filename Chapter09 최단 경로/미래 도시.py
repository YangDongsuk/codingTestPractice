INF=int(1e9)
n,m=map(int,input().split())
lst=[[INF]*(n+1) for i in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            lst[a][b]=0
for i in range(m):
    a,b=map(int,input().split())
    lst[a][b]=1
    lst[b][a]=1
x,k=map(int,input().split())

def flosial(n):
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                lst[a][b]=min(lst[a][b],lst[a][k]+lst[b][k])
                lst[b][a]=min(lst[b][a],lst[b][k]+lst[a][k])
flosial(n)

if (lst[1][k]==INF or lst[k][x]==INF):print(-1)
else:
    print(lst[1][k]+lst[k][x])
    
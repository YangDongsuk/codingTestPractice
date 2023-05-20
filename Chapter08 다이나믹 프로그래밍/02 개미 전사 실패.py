d=[[0,0]for i in range(101)]
#자기자신 포함이 0,미포함이 1
n=int(input())
lst=list(map(int,input().split()))
d[0][0]=lst[0]
d[0][1]=1
if lst[0]<lst[1]:
    d[1][0]=lst[1]
    d[1][1]=1
else:
    d[1][0]=lst[0]
    d[1][1]=0
if lst[0]+lst[2]<lst[1]:
    d[2][0]=lst[1]
    d[2][1]=0
else:
    d[2][0]=lst[0]+lst[2]
    d[2][1]=1

for i in range(3,n):
    if d[i-3][1]:
        d[i][0]=max(lst[i],lst[i-1])+d[i-3][0]
        if lst[i]>lst[i-1]:d[i][1]=1
        else:d[i][1]=0
    else:
        d[i][0]=max(lst[i]+lst[i-2],lst[i-1])+d[i-3]
        if lst[i]+lst[i-2]>lst[i-1]:d[i][1]=1
        else:d[i][1]=0
        
        
print(d[i])
print(d)
    

n=int(input())
d=[0]*1001
d[1]=1
d[2]=3
for i in range(3,n+1):
    d[i]=d[i-2]*2+d[i-1]
    #d[i]=(d[i-2]*2+d[i-1])%796796이게 좀 더 안전하다.
print(d[n]%796796)
    
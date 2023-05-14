n,m,k=map(int,input().split())
data=list(map(int,input().split()))
print(n,k,m)
print(data)
data.sort(reverse=True)
if (data[0]==data[1]):
    print(k*data[0])
else:
    print((m//(k+1))*(data[0]*k+data[1])+(m%(k+1)*data[0]))


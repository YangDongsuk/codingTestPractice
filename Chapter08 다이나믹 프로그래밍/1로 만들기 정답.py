x=int(input())

d=[0]*30001

#다이나믹 프로그래밍 보텀업
for i in range(2,x+1):
    #현재 수 -1
    d[i]=d[i-1]+1
    #현재 수/2
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)   
    #현재 수/3
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)  
    #현재 수/5
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)  
print(d[x])
print(d)
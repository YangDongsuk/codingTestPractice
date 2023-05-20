n=int(input())
count=0
while n!=1:
    if n%5==0:
        n/=5
        count+=1
    if n%3==0:
        n/=3
        count+=1
    if n%2==0:
        n/=2
        count+=1
    n-=1
    count+1
print(count)
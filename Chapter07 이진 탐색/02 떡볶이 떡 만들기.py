n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        sum=0
        for i in arr:
            if i<=mid:break
            sum+=(i-mid)
        if sum==target:
            return mid
        if sum<target:
            end=mid-1
        else:
            start=mid+1
    return mid
result=binary_search(arr,m,0,arr[0])
print(result)
    
            
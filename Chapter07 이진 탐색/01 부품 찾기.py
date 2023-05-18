n=int(input())
lst=list(map(int,input().split()))
lst.sort()
m=int(input())
order=list(map(int,input().split()))

def binary_search(arr,start,end,target):
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid
        if target<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return None
for i in order:
    result=binary_search(lst,0,len(lst)-1,i)
    if result!=None:print("yes")
    else:print("no")
        


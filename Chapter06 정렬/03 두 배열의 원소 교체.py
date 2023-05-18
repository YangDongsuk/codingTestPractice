n,k=map(int,input().split())
lst_A=list(map(int,input().split()))
lst_B=list(map(int,input().split()))
lst_A.sort()
lst_B.sort(reverse=True)
for i in range(k):
    lst_A[i],lst_B[i]=lst_B[i],lst_A[i]
print(sum(lst_A))
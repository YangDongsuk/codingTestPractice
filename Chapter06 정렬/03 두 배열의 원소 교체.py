n,k=map(int,input().split())
lst_A=list(map(int,input().split()))
lst_B=list(map(int,input().split()))
lst_A.sort()
lst_B.sort(reverse=True)
for i in range(k):
    
    if lst_A[i]<lst_B[i]:#이 조건을 반드시 넣어줘야함. 난 빼먹음
        lst_A[i],lst_B[i]=lst_B[i],lst_A[i]
    else: #얘도 빼먹음
        break
print(sum(lst_A))
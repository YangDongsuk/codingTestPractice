n,m=map(int,input().split())
lst=[]
count=0
for _ in range(n):
    lst.append(list(map(int,input().split())))

def dfs(lst,a,b):
    lst[a][b]=1
    case=[[a-1,b],[a+1,b],[a,b-1],[a,b+1]]
    for i in case:
        if 0<=i[0]<n and 0<=i[1]<m:
            if lst[i[0]][i[1]]==0:
                dfs(lst,i[0],i[1])

    

    
for i in range(n):
    for j in range(m):
        if lst[i][j]==0:
            count+=1
            dfs(lst,i,j)
print(count)
        
"""
정답 코드 넣는게 제일 힘든 문제
0 0 0 0 0 1 1 1 1 0 0 0 0 0
1 1 1 1 1 1 0 1 1 1 1 1 1 0
1 1 0 1 1 1 0 1 1 0 1 1 1 0
1 1 0 1 1 1 0 1 1 0 0 0 0 0
1 1 0 1 1 1 1 1 1 1 1 1 1 1
1 1 0 1 1 1 1 1 1 1 1 1 0 0
1 1 0 0 0 0 0 0 0 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 1 1 1 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 0 1 1
1 1 1 0 0 0 1 1 1 1 1 1 1 1 
1 1 1 0 0 0 1 1 1 1 1 1 1 1
"""    
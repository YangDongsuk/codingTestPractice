n,m=map(int,input().split())
lst=[]
visited=[[0]*m for _ in range(n)]
count=0
print(visited)
for _ in range(n):
    lst.append(list(map(int,input().split())))

def dfs(lst,visited,a,b):
    visited[a][b]=1
    case=[[a-1,b],[a+1,b],[a,b-1],[a,b+1]]
    for i in case:
        if 0<=i[0]<n and 0<=i[1]<m:
            if visited[i[0]][i[1]]==0:
                dfs(lst,visited,i[0],i[1])

    
for i in range(n):
    for j in range(m):
        if lst[i][j]==1:visited[i][j]=1
    
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            count+=1
            dfs(lst,visited,i,j)
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
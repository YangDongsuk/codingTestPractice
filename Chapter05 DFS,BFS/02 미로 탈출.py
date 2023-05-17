from collections import deque
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(graph,a,b):
    count=0
    graph[a][b]=0
    count+=1
    print(count)
    queue=deque([(a,b)])
    print(queue)
    while queue:
        v=queue.popleft()
        print(v,count)
        
        case=[[v[0]-1,v[1]],[v[0]+1,v[1]],[v[0],v[1]-1],[v[0],v[1]+1]]

        flag=1
        for i in case:
            if 0<=i[0]<n and 0<=i[1]<m:
                if i[0]==n-1 and i[1]==m-1:
                    count+=1
                    return count
                if graph[i[0]][i[1]]==1:
                    queue.append((i[0],i[1]))
                    print(queue)
                    graph[i[0]][i[1]]=0
                    if flag: 
                        count+=1
                        flag=0
                        
count=bfs(graph,0,0)
print(count)

"""
5 6
1 0 1 0 1 0 
1 1 1 1 1 1
0 0 0 0 0 1
1 1 1 1 1 1
1 1 1 1 1 1
"""
import heapq 
inf=int(1e9)
n,m,c=map(int,input().split())
distance=[inf]*(n+1)
graph=[[]for i in range(n+1)]
for i in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
distance[c]=0
q=[]
heapq.heappush(q,(0,c))
while q:
    now_distance,now=heapq.heappop(q)
    if now_distance>distance[now]:
        continue
    for i in graph[now]:
        if distance[i[0]]>(now_distance+i[1]):
            distance[i[0]]=now_distance+i[1]
            heapq.heappush(q,(distance[i[0]],i[0]))
answer=[]
for i in distance:
    if i!=inf and i!=0:
        answer.append(i)  
print(len(answer), end=" ")
print(max(answer))

        
    
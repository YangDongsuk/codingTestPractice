n,m=map(int,input().split())
dy,dx,ro=map(int,input().split())
game_map=[]
history=[[dy,dx]]
direction=[[-1,0],[0,1],[1,0],[0,-1]]
count=0
num=5
for _ in range(n):
    game_map.append(list(map(int,input().split())))
print(n,m)
print(dx,dy,ro)
print(game_map)

while 1:
    print("start")
    print(dx,dy, ro)
    flag=1
    for i in range(4):
        new_ro=(ro-i-1+4)%4
        new_dy=dy+direction[new_ro][0]
        new_dx=dx+direction[new_ro][1]
        print(new_dx,new_dy, game_map[new_dy][new_dx],new_ro, ":" ,history)
        if 0<=new_dx<m and 0<=new_dy<n:
            if game_map[new_dy][new_dx]==0 and [new_dy,new_dx] not in history:
                dx,dy=new_dx,new_dy
                ro=new_ro
                history.append([new_dy,new_dx])
                flag=0
                count+=1
                break
    if (flag):
        new_ro=(ro-2+4)%4
        new_dy=dy+direction[new_ro][0]
        new_dx=dx+direction[new_ro][1]
        if game_map[new_dy][new_dx]==1:
            break
        else:
            dx,dy=new_dx,new_dy
            count+=1
             
print(count)
        
        
    
        
    
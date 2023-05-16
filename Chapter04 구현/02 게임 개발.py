n,m=map(int,input().split())
dy,dx,wc=map(int,input().split())
game_map=[]
move_area=[]
direction=[[0,1],[1,0],[0,-1],[-1,0]]
count=0
num=5
for _ in range(n):
    game_map.append(list(map(int,input().split())))
print(n,m)
print(dx,dy,wc)
print(game_map)

def check_can_move(game_map,move_area,dx,dy):
    if 0<=dx+1<m:
        if game_map[dx+1][dy]==0 and [dx+1,dy] not in move_area:
            return 1
    if 0<=dx-1<m:
        if game_map[dx-1][dy]==0 and [dx-1,dy] not in move_area:
            return 1
    if 0<=dy+1<n:
        if game_map[dx][dy+1]==0 and [dx,dy+1] not in move_area:
            return 1
    if 0<=dy-1<n:
        if game_map[dx+1][dy-1]==0 and [dx,dy-1] not in move_area:
            return 1
    return 0
while num:
    result=check_can_move(game_map,move_area,dx,dy)
    print("result",result)
    if result:
        print("good")
        for i in range(3):
            my_dir=direction[(wc+4-i-1)%4]
            print("mydir",my_dir)
            print(dx+my_dir[0],dy+my_dir[1])
            if 0<=dx+my_dir[0]<m and 0<=dy+my_dir[1]<n:
                print("??")
                print(game_map[dx+my_dir[0]][dy+my_dir[1]])
                print([[dx+my_dir[0]],[dy+my_dir[1]]])
                if game_map[dx+my_dir[0]][dy+my_dir[1]]==0 and  [dx+my_dir[0],dy+my_dir[1]] not in move_area:
                    dx,dy=dx+my_dir[0],dy+my_dir[1]
                    wc=(wc+4-i-1)%4
                    count+=1
                    move_area.append([dx+my_dir[0],dy+my_dir[1]] )
                    print(dx,dy,wc,count,move_area)
                
    else:
        if (game_map[dx+direction[(wc+2)%4][0]][dy+direction[(wc+2)%4][1]])==1:
            break
        else:
            dx+=direction[(wc+2)%4][0]
            dy+=direction[(wc+2)%4][1]
            count+=1
    num-=1
print(count)
            
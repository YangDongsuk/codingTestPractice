n,k=map(int,input().split())
min_num=0
for _ in range(n):
    new_num=min(list(map(int,input().split())))
    if min_num<new_num:min_num=new_num
print(min_num)
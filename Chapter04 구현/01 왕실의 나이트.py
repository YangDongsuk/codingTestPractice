order=input()
order_dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,}
i=order_dict[order[0]]
#i=int(ord(order[0]))-int(ord('a'))+1로 해도 된다
j=int(order[1])
move=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
count=0
for k in move:
    if i+k[0]>0 and i+k[0]<9 and j+k[1]>0 and j+k[1]<9:count+=1
print(count)
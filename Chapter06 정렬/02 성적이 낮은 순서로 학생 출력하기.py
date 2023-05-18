n=int(input())
lst=[[] for i in range(101)]

print(lst)
for i in range(n):
    data=input().split()
    name=data[0]
    score=int(data[1])
    lst[score].append(name)
for i in range(101):
    for j in range(len(lst[i])):
        print(lst[i][j],end=" ")
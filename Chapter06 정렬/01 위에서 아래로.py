n=int(input())
sorted_lst=[]
for i in range(n):
    sorted_lst.append(int(input()))
sorted_lst.sort(reverse=True)
for i in sorted_lst:
    print(i, end=" ")
    
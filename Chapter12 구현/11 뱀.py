import copy
n = int(input())
k = int(input())

body = [[1, 1]]
apple = []
for i in range(k):
    a = list(map(int, input().split()))
    apple.append(a)
l_num = int(input())
l_list = []
for i in range(l_num):
    b = list(input().split())
    b[0] = int(b[0])
    l_list.append(b)

# print(n, apple, l_list)
time = 0
dir = 0
dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_head():
    global dir
    for i in l_list:
        # print("i", i, "time-1", time-1)
        if i[0] == time-1:
            # print("cd")
            if i[1] == "D":
                dir = (dir+1) % 4
            else:
                dir = (dir-1) % 4
            break
    new_head = copy.deepcopy(body)[0]
    # print("this", new_head)
    new_head[0] += dir_list[dir][0]
    new_head[1] += dir_list[dir][1]
    # print("new_head: ", new_head, "dir: ", dir)
    return new_head


def collision(new_head):
    if new_head[0] < 1 or new_head[0] > n or new_head[1] < 1 or new_head[1] > n:
        # print("case1")
        return 1
    if new_head in body:
        # print("case2")
        # print(new_head, body)
        return 1
    return 0


while 1:
    time += 1
    # print("time", time)
    new_head = get_head()
    if collision(new_head):
        print(time)
        break
    body = [new_head]+body
    check = 1
    for i in range(len(apple)):
        if new_head == apple[i]:
            apple.pop(i)
            check = 0
            break
    if check:
        body.pop()

    # print("body", body)

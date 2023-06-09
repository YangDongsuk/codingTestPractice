
def solution(key, lock):
    keys = []
    arr = key
    print(arr)
    for _ in range(4):
        arr = make_ro(arr)
        print("arr", arr)
        keys.append(arr)


    answer = True
    return key, lock


def make_ro(arr):
    ro = [[0]*len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            ro[j][-i-1] = arr[i][j]

    return ro

def check_Lock(key, lock):
    
    for w in range()
    able=True
    for i in range(len(lock)):
        for j in range(len(lock)):
            if key[i][j]==1:
                if lock[i][j]==0:
                    lock[i][j]=1
                else:
                    able=False
    if able:
        if sum(lock)==len(lock)*len(lock):
            return True
    return False
    
                
    


solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)


[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

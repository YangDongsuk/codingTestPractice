dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(100):
    print(dir_list[(-i) % 4])

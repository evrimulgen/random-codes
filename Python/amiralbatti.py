import pdb
base = [
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
        ]


x = " x "

def print_base():
    for i in range(10):
        for j in range(10):
            print(base[i][j],end="\n" if j==9 else "")


def choice_position(pos_start, direction, gemi_buyuklugu=4):
    # print(pdb)
    # pdb.set_trace()
    pos_start = pos_start.split(" ")
    base[int(pos_start[0])][int(pos_start[1])] = [1]
    pos_start_dir = int(pos_start[0])
    if direction == "kuzey":
        for i in range(gemi_buyuklugu):
            pos_start_dir = pos_start_dir - 1
            base[int(pos_start_dir)][int(pos_start[1])] = [1]
    if direction == "guney":
        for i in range(gemi_buyuklugu):
            pos_start_dir = pos_start_dir + 1
            base[int(pos_start_dir)][int(pos_start[1])] = [1]
    if direction == "dogu":
        for i in range(gemi_buyuklugu):
            pos_start_dir = pos_start_dir + 1
            base[int(int(pos_start[0]))][int(pos_start_dir)] = [1]
    if direction == "bati":
        for i in range(gemi_buyuklugu):
            pos_start_dir = pos_start_dir - 1
            base[int(int(pos_start[0]))][int(pos_start_dir)] = [1]

    print_base()


choice_position(input("5li gemiyi nereye koymak istersin?"), direction=input("yon ne? (kuzey, guney, dogu, bati)"))
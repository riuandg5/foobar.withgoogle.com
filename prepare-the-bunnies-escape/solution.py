import numpy as np

def solution(map):
    # Your code here
    map = np.array(map)
    h,w = map.shape
    walls_x, walls_y = np.where(map==1)
    min_steps = 10000

    for i in range(len(walls_x)+1):
        board = np.full((h,w), None)
        if (i==0):
            board[walls_x, walls_y] = -1
        else:
            board[np.delete(walls_x, -i), np.delete(walls_y, -i)] = -1

        board[h-1, w-1] = 1
        fill = 1
        progress = 1

        while (progress == 1 and board[0,0] == None):
            progress = 0
            for x in range(h):
                for y in range(w):
                    if (board[x,y] == fill):
                        if (y-1>=0 and board[x,y-1]==None):
                            board[x,y-1] = fill+1
                            progress = 1
                        if (x-1>=0 and board[x-1,y]==None):
                            board[x-1,y] = fill+1
                            progress = 1
                        if (y+1<w and board[x,y+1]==None):
                            board[x,y+1] = fill+1
                            progress = 1
                        if (x+1<h and board[x+1,y]==None):
                            board[x+1,y] = fill+1
                            progress = 1
            fill = fill + 1

        if (board[0,0] != None):
            if (board[0,0] < min_steps):
                min_steps = board[0,0]
    
    return min_steps
def solution(src, dest):
    #Your code here
    size = 8
    board = [[None for i in range(size)] for j in range(size)]

    board[src//size][src%size] = 0
    fill = 0

    while (board[dest//size][dest%size] == None):
        for i in range(size):
            for j in range(size):
                if (board[i][j] == fill):
                    if (i+2<size and j+1<size and board[i+2][j+1]==None):
                        board[i+2][j+1] = fill+1
                    if (i+2<size and j-1>=0 and board[i+2][j-1]==None):
                        board[i+2][j-1] = fill+1

                    if (i-2>=0 and j+1<size and board[i-2][j+1]==None):
                        board[i-2][j+1] = fill+1
                    if (i-2>=0 and j-1>=0 and board[i-2][j-1]==None):
                        board[i-2][j-1] = fill+1

                    if (i+1<size and j+2<size and board[i+1][j+2]==None):
                        board[i+1][j+2] = fill+1
                    if (i-1>=0 and j+2<size and board[i-1][j+2]==None):
                        board[i-1][j+2] = fill+1

                    if (i+1<size and j-2>=0 and board[i+1][j-2]==None):
                        board[i+1][j-2] = fill+1
                    if (i-1>=0 and j-2>=0 and board[i-1][j-2]==None):
                        board[i-1][j-2] = fill+1
                        
        fill = fill + 1

    return board[dest//size][dest%size]
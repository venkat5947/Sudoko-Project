sudoko_board=[
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]
def find_empty_cell(sudoko_board):
    
    for i in range(9):
        for j in range(9):
            if sudoko_board[i][j]==0:
                return [i,j]
    return None

def valid_or_not(sudoko_board,number,position):
    for j in range(9):
        if sudoko_board[position[0]][j]==number and position[1]!=j:
            return False
    for i in range(9):
        if sudoko_board[i][position[1]]==number and position[0]!=i:
            return False
    p=position[0]//3
    q=position[1]//3
    for i in range(p*3,p*3+3):
        for j in range(q*3,q*3+3):
            if sudoko_board[i][j]==number and [i,j]!=position:
                return False
    return True



def solve_board(sudoko_board):
    x=find_empty_cell(sudoko_board)
    if x==None:
        return True
    for i in range(1,10):
        if valid_or_not(sudoko_board,i,x):
            sudoko_board[x[0]][x[1]]=i

            if(solve_board(sudoko_board)):
                return True
            sudoko_board[x[0]][x[1]]=0
    return False
print("Before")
for i in sudoko_board:
    print(*i)

print()
print()

solve_board(sudoko_board)

print("After")
for i in sudoko_board:
    print(*i)


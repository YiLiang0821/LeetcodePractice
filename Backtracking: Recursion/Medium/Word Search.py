#79
def checkBound(board, x, y):
    if 0 <= x < len(board) and 0 <= y <len(board[0]):
        return True
    else:
        return False

def wordSearch(board, word, x, y, n):
    if not checkBound(board, x, y) or word[n] != board[x][y]:
        return False
    if n == len(word) - 1:
        return True
    #mark the board that we checked
    charToCheck = board[x][y]
    board[x][y] = 0
    # search neighbor
    for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        # if xx < 0 or yy < 0 or xx > len(board) or yy > len(board[0]):
        #         continue
        if wordSearch(board, word, xx, yy, n+1):
            return True
    #Resume travel this time
    board[x][y] = charToCheck
    

def exist(board, word):
    if len(board) == 0:
        return False
    word = list(word)

    for x in range(len(board)):
        for y in range(len(board[0])):
            if wordSearch(board, word, x, y, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word))
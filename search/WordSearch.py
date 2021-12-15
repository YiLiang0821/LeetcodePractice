#79
def wordSearch(board, word):
    word = list(word)
    for x in range(len(board)):
        for y in range(len(board[0])):
            if search(board, word, x, y, 0):
                return True
    return False

def search(board, word, x, y, n):
    if (x < 0 or x >=len(board) or y < 0 or  y >=len(board[0]) or word[n] != board[x][y]):
        return False
    if n == len(word) - 1:
        return True
    tmpChar = board[x][y] #同格子不能使用多次
    board[x][y] = 0 #這個不能走了
    
    for xx, yy in [(x+1, y), (x-1, y),(x, y+1),(x, y-1)]: #x and 的上下左右
        if search(board, word, xx, yy, n+1):
            return True
    board[x][y] = tmpChar #退出這次上下左右遞迴 復原這格 代表可以走了

    



def not_inBound(x, y):
    if x < 0 or x >=len(board) or y < 0 or  y >=len(board[0]):
        return False
    else: return True


board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = 'ABCCED'

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"

board3 = [["C","A","A"],["A","A","A"],["B","C","D"]]
word3 = "AAB"

board4 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word4 = "ABCB"

print(wordSearch(board4, word4))


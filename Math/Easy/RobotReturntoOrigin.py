# 657
def judgeCircle(moves):
    if moves.count('U') != moves.count('D') or moves.count('L') != moves.count('R'):
        return False
    return True

'''
TC is O(4 * n) = O(n)
SC is O(1)
'''
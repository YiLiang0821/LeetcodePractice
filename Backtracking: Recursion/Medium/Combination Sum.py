#39
# basic search all combination
def backTrack(candidates, target, ans, cur, index, sumCurr):
     #stop condition: sum(cur) == target or sum(cur) > target
    if sumCurr == target:
        ans.append(cur[:])

    elif sumCurr < target:
        # avoid [2,6] [6,2]
        for i in range(index, len(candidates)):
            cur.append(candidates[i])
            backTrack(candidates, target, ans, cur, i, sumCurr+ candidates[i])
            #iterate candidates[i]
            #[2] -> [2,2],[2,3],[2,6]
            cur.pop() # pop out the candidates[i] which push previous and try next one
    
    return 
def combinationSum(candidates, target):
    ans = []
    cur = []
    backTrack(candidates, target, ans, cur, 0, 0)
    return ans

candidates = [2,3,6]
target = 8
print(combinationSum(candidates, target))
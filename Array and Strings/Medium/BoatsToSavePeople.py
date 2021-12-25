#881
# key is sorted the people first
def BoatsToSavePeople(people, limit):
    #people.sort()
    people = sorted(people)
    L = 0
    R = len(people) - 1
    boats = 0
    while( L <= R):
        if (L == R):                                    #One left
            boats += 1
            break
        elif( people[L] + people[R] <= limit):
            L += 1
            
        R -= 1
        boats += 1
    return boats
print(BoatsToSavePeople([3,5,3,4], 5))
'''
TC is O(nlog(n)), due to sort algo O(nlong(n)) + loop over array O(n) -> O(nlong(n))
SC is O(n) sort internally use algo that has O(n) sc
'''
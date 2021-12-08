#49
def groupAnagrams(strs):
    anagrams = {}
    output =[]

    for i in strs:
        item = ''.join(sorted(i)) # list can't be hashed
        if item not in anagrams:
            anagrams[item] = []
        anagrams[item].append(i)
    for j in anagrams.values():
        output.append(j)

    return output
    
strs = ["eat","tea","tan","ate","nat","bat"]       
print(groupAnagrams(strs))

'''
TC is O(n * m * log(m))
n: length of the input array
m: length of biggest string in the array 
-> sorted : m * log (m)

SC is O(n) -> use hash map
'''
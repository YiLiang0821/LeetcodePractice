import random
data = random.sample(range(100),10)
data = sorted(data)

def binarySerach(data, target):
    lower = 0
    upper = len(data) - 1
    searchCount = 0
    if target < data[lower] or target > data[upper]:
        return('out of range')
    else:
        while(lower <= upper):
            searchCount += 1
            mid = (lower + upper) // 2 #index
            if target < data[mid]: #left side
                upper = mid - 1
            elif target > data[mid]: #compare value
                lower = mid + 1      # index control range
            else:
                return data[mid], searchCount
        return('no this value')
print(data)
print(binarySerach(data, 20))

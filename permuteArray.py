
#incomplete program , still working on it 
def permute(arrList):
    
    if arrList is None or len(arrList) == 0:
        return None
    
    nlen = len(arrList)
    indices = [0] * nlen
    results  = list()
    permuteArray(arrList, nlen, indices, results)
    
    return results

def permuteArray(arrList, nlen, indices, result):
    op = [0] * nlen
    for x in range(nlen):
        arr = arrList[x]
        index = indices[x]
        op[x] = arr[index]
        
    result.append(op)
    ptr = nlen - 1
    while indices[ptr] == len(arrList[ptr]) - 1:
        ptr = ptr - 1
        if ptr < 0:
            return
    
    indices[ptr]+=1
    if ptr == 0:
        #reset rest other indices to 0
        for x in range(1, nlen):
            indices[x] = 0
            
            
    permuteArray(arrList, nlen, indices, result)

arrList = [[1], [2, 3], [4], [5, 6]]
print permute(arrList)
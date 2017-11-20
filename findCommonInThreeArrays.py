'''
Now we are coming on territory of tough array questions. Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples:

input1 = {1, 5, 10, 20, 40, 80}
input2 = {6, 7, 20, 80, 100}
input3 = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80

Iterate through a1 and a2 to output a common list
binary search the common list on the 3rd array

'''

#create an array of size n - 1
#iterate through given input 

def findCommon(num1, m, num2, n):
    
    if m == 0 or n == 0:
        return None
    
    i ,j, k = 0, 0, 0
    
    common = list()
    while i < m and j < n:
        if num1[i] == num2[j]:
            common.append(num1[i])
            i +=1
            j +=1
        elif num1[i] < num2[j]:
            i += 1
        else:
            j += 1
        
    return common
    

def bsearch(num, k):
    
    if num is None or len(num) == 0:
        return -1
    
    lo = 0
    hi = len(num) - 1
    mid = 0
    
    while lo <= hi:
        mid = lo + (hi - lo)/2
        if num[mid] == k:
            return mid
        elif num[mid] < k:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return -1
    

def printCommon(num1, num2, num3):
    
    k = len(num1)
    l = len(num2)
    m = len(num3)
    
    maxLen = max(k, max(l, m))
    a1 = None
    a2 = None
    a3 = None
    
    if maxLen == k :
        a1 = num2
        a2 = num3
        a3 = num1
    elif maxLen == l:
        a1 = num1
        a2 = num3
        a3 = num2
    else:
        a1 = num1
        a2 = num2
        a3 = num3
    
    common = findCommon(a1, len(a1), a2, len(a2))
    result = list()
    
    if common is not None or len(common) != 0 :
        for x in range(len(common)):
            k = common[x]
            if bsearch(a3, k) != -1:
                result.append(k)
    
    print(result)



input1 = [1, 5, 10, 20, 40, 80]
input2 = [6, 7, 20, 80, 100]
input3 = [3, 4, 15, 20, 30, 70, 80, 120]
printCommon(input1, input2, input3)
    
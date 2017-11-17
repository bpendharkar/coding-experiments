# Given an array of float numbers, use arithmetic operators to find the max value 
# Consider an equal operator precedence and the array is scanned from left to right
# e.g. # [1 12 -3] =>  max is 33 => 1 - 12 * 3 

# calculate 4 values , check the min and max value
# calculate 8 values , check min and max values

#-1 -2  3 =>  [ -3, 1, 2, -.5] => [ 2, -3] , 3 => [ 5, -1, 6, .667, 0, -6, -9, -1] => 6
# 1 12 -3 =>  [ 13, -11, .0825, 12] => [13, -11] -3 => 

def calculateMathOps(a, b):
    
    result = [a+b, a-b, a*b, 0]
    if b != 0:
        result[3] = a/b
    
    return result

def calculateMinMax(nums):
    
    n = len(nums)
    if n > 0:
        minVal = nums[0]
        maxVal = nums[0]
    else:
        return []
    
    for x in range(1, n):
        
        if nums[x] < minVal:
            minVal = nums[x]
        if nums[x] > maxVal:
            maxVal = nums[x]
        
    return [maxVal, minVal]
        

def findMaxValue(floatNums):
    
    if floatNums is None or len(floatNums) == 0:
        return 0
    
    n = len(floatNums)        
    if n == 1:
        return floatNums[0]
           
    op = None
    result = 0    
    
    a = floatNums[0]
    b = floatNums[1]
        
    mathResult = calculateMathOps(a, b)
    maxMinArray = calculateMinMax(mathResult)
    
    
    for x in range(2, n):
        
        #calculate all possible combinations
        k = floatNums[x]
        
        arrOne = calculateMathOps(maxMinArray[0], k)
        arrTwo = calculateMathOps(maxMinArray[1], k)        
        arrOne.extend(arrTwo)
        
        maxMinArray = calculateMinMax(arrOne)
        
    
    return maxMinArray[0]


print(findMaxValue([-21, 6, 9, -43]))
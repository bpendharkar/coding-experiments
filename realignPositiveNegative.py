'''
How to rearrange array in alternating positive and negative number? (solution)
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array. This is also a difficult array problem to solve and you need lot of practice to solve this kind of problems in real interviews, especially when you see it first time. If you have time constraint then always attempt these kind of questions once you are done with easier ones. 

Example:

Input: {1, 2, 3, -4, -1, 4}
Output: {-4, 1, -1, 2, 3, 4}

Input: {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0} 


Read more: http://javarevisited.blogspot.com/2015/06/top-20-array-interview-questions-and-answers.html#ixzz4yqYzAIja

rearranging numbers : 
first scan to determine the count of positives and negatives 

if positive are more, the first no should be negative
scan the array for first negative , if it is not in odd pos, swap it with odd pos

'''

def replacePosNeg(nums):
    
    if nums is None or len(nums) == 0:
        return
    
    n = len(nums)
    
    #move all negatives to one side , move all positives
    def swap(x, y):
        c = nums[x]
        nums[x] = nums[y]
        nums[y] = c
    
    y= -1
    for x in range(n):
        
        if nums[x] < 0 :
            y += 1
            swap(x, y)

    p2 = y + 1
    p3 = 0
    while p3 < p2 and p2 < n and nums[p3] < 0:
        swap(p3, p2)
        p3 +=2
        p2 +=1
    
    print(nums)
            
nums = [2, 8, 9, 1 ,1, 2, 3, -4 , 4, -3, -5 , -9, -8, 7, -6 , 9, -13, -25, 4, 5, 6,7 , 8]
replacePosNeg(nums)

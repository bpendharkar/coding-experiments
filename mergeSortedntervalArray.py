'''
Merge 2 arrays of sorted intervals as a single array of intervals 

Given: 
Arr1 = [3-11, 17-25, 58-73]; 
Arr2 = [6-18, 40-47]; 

Wanted: 
Arr3 = [3-25, 40-47, 58-73];
'''

def mergeSortedInterval(nums1, nums2):
    
    if nums1 is None and nums2 is None or len(nums1) == 0 and len(nums2) == 0:
        return None
    
    if nums1 is None:
        return nums2
    
    if nums2 is None:
        return nums1
    
    p1 = p2 = 0
    mergedIntervals = list()
    
    while p1 < len(nums1) and p2 < len(nums2):
        s1 = nums1[p1][0]
        e1 = nums1[p1][1]
        
        s2 = nums2[p2][0]
        e2 = nums2[p2][1]
        
        if s1 <= s2:
            if e1 >= s2 :
                # interval is merging with s1 as beginning                
                e = e1 if e1 > e2 else e2
                mergedIntervals.append([s1, e])
                p1 += 1
                p2 += 1
            else:
                mergedIntervals.append([s1, e1])
                p1 += 1    	
        else:
            if e2 >= s1:
                #interval is merging with s2 as begining
                e = e1 if e1 > e2 else e2
                mergedIntervals.append([s2, e])
                p1 += 1
                p2 += 1
            else:
                mergedIntervals.append([s2, e2])
                p2 += 1
           
    #end while
    
    while p1 < len(nums1):
        mergedIntervals.append(nums1[p1])
        p1 += 1
    
    while p2 < len(nums2):
        mergedIntervals.append(nums2[p2])
        p2 += 1
    
            
    #merge the intervals in result
    intervalOp = list()
    intervalOp.append(mergedIntervals[0])
    i = 1
	
    # you have a sorted list of intervals and need to merge them
    while i < len(mergedIntervals):
        current = mergedIntervals[i]
        opLen = len(intervalOp)
        lastMergedInterval = intervalOp[opLen - 1]
        
        #check if start of current interval is smaller than earlier
        if current[0] <= lastMergedInterval[1]:
            #we have a merge
            intervalOp.pop()
            end = lastMergedInterval[1] if lastMergedInterval[1] > current[1] else current[1]
            intervalOp.append([lastMergedInterval[0], end])
        else:
            #simply append the current 
            intervalOp.append(current)
        
        i+=1
       
        
    return intervalOp

nums1 = list()
nums1.append([3,10])
nums1.append([17,20])
nums1.append([26,50])
nums1.append([58,73])
nums2 = list()
nums2.append([6, 18])
nums2.append([40, 57])
nums2.append([58, 70])
nums2.append([70, 80])
print mergeSortedInterval(nums1, nums2)

intervals = [(2,5), (0,1), (3, 9), (7, 10)]
print intervals

def findminrooms(intervals):
    #[(0, 1)]
    if intervals is None or len(intervals) == 0 :
        return 0

    intervals = sorted(intervals)
    i = 1
    start = 0
    end = 1
    mincount = 1
    ct = 1
    
    merged = list()
    merged.append(intervals[0])    
    
    while i < len(intervals):
        current = intervals[i]
        previous = merged[len(merged)- 1]

        curr_s = current[start]
        curr_e = current[end]

        prev_s = previous[start]
        prev_e = previous[end]

        #check for overlap
        if prev_e > curr_s:
            
            #update the merged list            
            merged.pop() #removes previous
            newstart = prev_s
            newend = curr_e if curr_e > prev_e else prev_e
            merged.append((newstart, newend))            
            ct += 1
            if ct > mincount:
                mincount = ct
        else:
            merged.append(current)
            ct = 1

        i +=1

    print mincount
            
findminrooms(intervals)
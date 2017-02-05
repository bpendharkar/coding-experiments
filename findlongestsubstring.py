
#find longest substring with k distinct characters

def findlongestsubstring(s, k):

    if s is None or len(s) == 0:
        return None
       
    n = len(s)
    chCount = [0]* 256
    tracker = 0
    start = 0 
    end = 0
    newCharList = list()
    maxlen = 0
    maxend = 0
    maxstart = 0
    while end < n:
    
        if len(newCharList) != 0 :
            #shift the window and reduce tracker by 1
            start = newCharList.pop(0) # fetching the first element which had the new character
            if k > 1:
              asciiVal = ord(s[start])
              chCount[asciiVal] = 0
            tracker -=1
        else:                     
            end = start
            
        while end < n and tracker  <= k :
            c = s[end]
            asciiVal = ord(c)
            if chCount[asciiVal] == 0:
                #new char found
                chCount[asciiVal] = 1
                tracker +=1
                if end != 0:
                    newCharList.append(end)
            end +=1
        
        #we have substring from start to end - 1
        if end - start > maxlen:
            maxlen = end - start
            maxstart = start
            maxend = end 
            print(s[maxstart : maxend])
     
    return s[maxstart : maxend]
  
c = findlongestsubstring("aaaabbbbbbcdeeefffffffffffffff", 2)
print(c)

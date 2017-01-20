

s = "12345"

dc = {}
dc["1"] = "a"
dc["2"] = "b"
dc["3"] = "c"
dc["4"] = "d"
dc["5"] = "e"
dc["12"] = "l"
dc["23"] = "w"

def encodeString(s):
    if s is None or len(s) == 0:
        return None
    
    result = list()
    op = ""
    index = 0
    encodeStringUtil(s, op, index, result)
    
    return result

def encodeStringUtil(s, op, index, result):    
    if index == len(s):        
        result.append(op)
        return
    
    for x in range(2):
        if index + x > len(s) - 1:
            continue
        
        substr = ""
        if x == 0:
            substr = s[index]
        else:        
            substr = s[index: index + x + 1] 
                
        val = int(substr)
        
        if val >= 1 and val <= 26:
            dcVal = dc[substr]
            newop = op + dcVal
            newIdx = index + len(substr)            
            encodeStringUtil(s, newop, newIdx, result)

print encodeString(s)

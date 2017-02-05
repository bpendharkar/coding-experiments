
#determine if a string represented by moves "<^>v" results in a cycle and output all cycles

def outputCycles(directions):
    
    dc = dict()
    dc['<'] = [-1, 0]
    dc['>'] = [ 1, 0]
    dc['^'] = [ 0, 1]
    dc['v'] = [ 0,-1]
    
    
    positions = list()
    positions.append([0, 0])
    result = list()
    
    n = len(directions)
    i = 0
    while i < n:
        c = directions[i]        
        x = dc[c][0]
        y = dc[c][1]
        p = len(positions)
        newpos = [0, 0]
        newpos[0] =  positions[p - 1][0] + x
        newpos[1] =  positions[p - 1][1] + y
        
        
        if newpos in positions:
            #append the substring
            idx = positions.index(newpos)
            #substring = > idx to i
            result.append(directions[idx : i + 1])
            positions[idx] = [-1, -1]
        
        positions.append(newpos)
        i +=1
        
        
        
    return result
    
    
s = "^>v<^"
print(outputCycles(s))

def heappush(hp, x):
    if hp is None :
        hp = list()
        return
    if len(hp) == 0:        
        hp.append(x)
        return
        
    hp.append(x)    
    for x in range(len(hp)/2):
        heapify(hp, x)
    
def heappop(hp):
    if hp is None or len(hp) == 0:
        raise ValueError("Empty heap")
        
    val = hp.pop(0)
    heapify(hp, 0)
        
    return val
    
    
def heapifylist(hp):
    if hp is None or len(hp) == 0:
        return
    h = list()
    
    for x in range(0, len(hp)):
        heappush(h, hp[x])
    return h
            
    
def heapify(hp, x):        
    if len(hp) == 0:
        return
    
    left = 2*x + 1
    right = 2*x + 2    

    minelem = x
    if left < len(hp) and hp[left] < hp[minelem]:
        minelem = left        
    if right < len(hp) and hp[right] < hp[minelem]:
        minelem = right        
        
    if minelem != x :
        tmp = hp[x]
        hp[x] = hp[minelem]
        hp[minelem] = tmp        
        heapify(hp, minelem)

    
lst = [3, 4, 1, 6, 7, 8, 9, 2]
print heapifylist(lst)

h = list()
for k in range(len(lst)):    
    heappush(h, lst[k])

print h
def findlongestsub(s):
    
    if s is None or len(s) == 0:
        return None
    
    hset = set()
    p1 = p2 = 0
    maxlen = maxp1 = maxp2 = 0
    slen = len(s)
    
    while p2 < slen:
        c = s[p2]
        if c not in hset:
            hset.add(c)
            if (p2 - p1 + 1) > maxlen:
                maxlen = p2 - p1 + 1
                maxp1 = p1
                maxp2 = p2
        else:
            while c in hset and p1 < slen:
                d = s[p1]
                hset.remove(d)
                p1 = p1 + 1
            hset.add(c)
        p2 = p2 + 1
        
    return s[maxp1:maxp2 + 1]

print findlongestsub('acbca')
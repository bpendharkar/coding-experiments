def isdelimitermatching(s):
    
    if s is None or len(s) == 0:
        return True
    
    slen = len(s)
    a1 = ['(', '[', '{']
    oset = set(a1)
    a2 = [')', ']', '}']
    cset = set(a2)
    
    dc = dict()
    dc[')'] = '('
    dc[']'] = '['
    dc['}'] = '{'
    
    i = 0
    stack = list()
    while i < slen:
        c = s[i]
        if c in oset:
            stack.append(c)
        elif c in cset:
            if len(stack) == 0:
                return False
            d = stack.pop()
            if d not in oset:
                return False
            if dc[c] != d:
                return False
        i = i + 1
    
    if len(stack) != 0:
        return False
    
    return True

s = '[dklf(df(kl))d]{}'
print isdelimitermatching(s)   
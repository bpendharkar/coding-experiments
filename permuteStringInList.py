
''' Permute each char '''

def permuteUtil(lst, op, index):
    
    if len(op) == len(lst):
        print op
        return
    
    if index == len(lst):
        return
    
    word = lst[index]
    for i in xrange(len(word)):
        res = op + word[i]
        permuteUtil(lst, res, index + 1)
    

def permute(lstOfStr):    
    if lstOfStr is None or len(lstOfStr) == 0:
        return 
    
    n = len(lstOfStr)
    op = ""
    permuteUtil(lstOfStr, op, 0)

	
	    
lst = ["red", "fox", "super"]
permute(lst)

''' 
======= output =========
rfs
rfu
rfp
rfe
rfr
ros
rou
rop
roe
ror
rxs
rxu
rxp
rxe
rxr
efs
efu
efp
efe
efr
eos
eou
eop
eoe
eor
exs
exu
exp
exe
exr
dfs
dfu
dfp
dfe
dfr
dos
dou
dop
doe
dor
dxs
dxu
dxp
dxe
dxr

'''
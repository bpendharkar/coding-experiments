def canJump(self, nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	
	if nums is None or len(nums) == 0:
		return False
	
	nlen = len(nums)
	table = [False] * nlen
	table[nlen - 1] = True
	lastIndex = nlen - 1
	#mark table index as true for last one
	#lastindexreachable = n - 1
	#as you move down the array , check for value at index and check if index + val >= lastindexreachable
	#if so, update the lastindexreachable
	
	for x in xrange(nlen - 2, -1, -1):
		val = nums[x]
		if (x + val) >= lastIndex:
			table[x] = True
			lastIndex = x
	
	return table[0]
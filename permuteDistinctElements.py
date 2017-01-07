class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if nums is None or len(nums) == 0:
            return None
        
        result = list()
        nlen = len(nums)
        op = list()
        self.permuteArray(nums, nlen, op, result)
        return result
        
    def permuteArray(self, nums, nlen, op, result):
        if len(op) == nlen:
            result.append(list(op))
            return
        
        for x in range(nlen):
            if nums[x] in op:
                continue
            op.append(nums[x])
            self.permuteArray(nums, nlen, op, result)
            op.pop()
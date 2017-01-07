class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if nums is None or len(nums) == 0:
            return -1
        
        nlen = len(nums)
        lo = mid = 0
        hi = nlen - 1
        
        while lo <= hi:
            mid = lo + (hi - lo)/2
            if nums[mid] == target:
                return mid
            
            if nums[hi] < nums[mid]:
                if target <= nums[hi] or target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif nums[lo] > nums[mid]:
                if target >= nums[lo] or target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
        
        return -1
        
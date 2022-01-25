class Solution:
    def isPossible(self, nums, mid, m):
	    cnt = 1
	    sumAllocated = 0
	    for i in range(len(nums)):
		    if(sumAllocated > mid):
			    return False
		    sumAllocated += nums[i]
		    if(sumAllocated > mid):
			    cnt += 1
			    sumAllocated = nums[i]
	    if (cnt <= m):
		    return True
	    return False

    def splitArray(self, nums: List[int], m: int) -> int:
	    if m > len(nums):
		    return -1
	    low = max(nums)
	    high = sum(nums)
	    ans = 0
	    while low <= high:
		    mid = (low+high) >> 1
		    if self.isPossible(nums, mid, m):
			    ans = mid
			    high = mid-1
		    else:
			    low = mid+1
	    return ans

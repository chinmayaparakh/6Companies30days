class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        curr=rst=st=0
        ren=1000000000
        for i in range(n):
            curr+=nums[i]
            while curr>=target and st<=i:
                if ren-rst>i-st:
                    ren=i
                    rst=st
                curr-=nums[st]   
                st+=1           
        if ren==1000000000:
            return 0
        return ren-rst+1  

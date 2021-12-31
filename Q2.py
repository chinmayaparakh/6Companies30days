class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        #code here -21 26 89 4 -17 4 41 -73
        if R1[0] < L2[0] or L1[1] < R2[1] or R2[0] < L1[0] or R1[1] > L2[1]:
            return 0
        return 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        s=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1],s[0],s[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.doOverlap(p,q,r,s)
        print(ans)
# } Driver Code Ends

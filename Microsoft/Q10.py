
class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        if n==1:
            return a[0]
        elif n==2:
            return max(a[0],a[1])
        ans=[]
        ans.append(a[0])
        ans.append(a[1])
        ans.append(a[0]+a[2])
        for i in range(3,n):
            ans.append(a[i]+max(ans[i-2],ans[i-3]))
        return max(ans[-1],ans[-2])

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends

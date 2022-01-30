class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        #code here
        dp = [[0 for _ in range(b)] for _ in range(a)]
        for i in range(a):
            dp[i][-1]=1
        for j in range(b):
            dp[-1][j]=1
        
        
        for i in range(a-2,-1,-1):
            for j in range(b-2,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends

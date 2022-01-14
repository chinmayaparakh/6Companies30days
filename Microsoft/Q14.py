
class Solution:
    def minSteps(self, D):
        # code here
        sm=0
        st=1
        while True:
            sm+=st
            if sm==D:
                return st
            if sm>D and (sm-D)%2==0:
                return st
            st+=1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        D = int(input())
        
        ob = Solution()
        print(ob.minSteps(D))
# } Driver Code Ends

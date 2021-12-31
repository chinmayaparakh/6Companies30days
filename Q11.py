class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr.sort()
        out=[0,0]
        for i in range(0,n-1):
            if arr[i]==arr[i+1]:
                out[0]=arr[i]
                
        out[1]=(n*(n+1)//2)-(sum(arr)-out[0])
        return out 
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends

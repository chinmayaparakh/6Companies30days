#User function Template for python3
class Solution:
    def sots(self,arr):
        n=len(arr)
        for i in range(n):
            min_indx=i
            for j in range(i+1,n):
                if arr[min_indx]>arr[j]:
                    min_indx=j
            arr[i],arr[min_indx]=arr[min_indx],arr[i]
        return arr

	def matchPairs(self,nuts, bolts, n):
		# code here
		self.sots(nuts)
        self.sots(bolts)

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends

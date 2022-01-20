import heapq
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        # code here
        # print the smallest range in a new line
        minheap=[]
        maxx=-float('inf')
        for i in range(k):
            heapq.heappush(minheap,(KSortedArray[i][0],i,0))
            maxx=max(KSortedArray[i][0],maxx)
        heapq.heapify(minheap)
        diff=maxx-minheap[0][0]
        ans=[minheap[0][0],maxx]
       
        while True:
            mini,r,c=heapq.heappop(minheap)
            if diff>maxx-mini:
                diff=maxx-mini
                ans=[mini,maxx]
            if c+1>=len(KSortedArray[r]):
                break
            num=KSortedArray[r][c+1]
            maxx=max(maxx,num)
            heapq.heappush(minheap,(num,r,c+1))
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    KSortedArray=[]
    for i in range(k):
        KSortedArray.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(KSortedArray, n, k)
    print(r[0],r[1])
# } Driver Code Ends

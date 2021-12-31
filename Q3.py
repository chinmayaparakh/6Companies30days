class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        n = len(a)
        p = 1
        res = 0
        start = 0
        end = 0
        while(end < n):
            p *= a[end]
            while (start < end and p >= k):
                p = int(p//a[start])
                start += 1
            if (p < k):
                l = end - start + 1
                res += l
     
            end += 1
     
        return res
                
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends

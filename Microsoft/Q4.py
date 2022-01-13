class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,mat, r, c): 
        # code here 
        ur=lc=0
        dr=r-1
        rc=c-1
        ans=[]
        if r==1:
            i=j=0
            while j<=rc:
                ans.append(mat[i][j])
                j+=1
            return ans
        elif c==1:
            i=j=0
            while i<=dr:
                ans.append(mat[i][j])
                i+=1
            return ans
        while ur<=dr and lc<=rc:
            i=ur
            j=lc
            while j<=rc:
                ans.append(mat[i][j])
                j+=1
            if ur==dr:
                break
            j-=1
            i+=1
            while i<=dr:
                ans.append(mat[i][j])
                i+=1
            if lc==rc:
                break
            i-=1
            j-=1
            while j>=lc:
                ans.append(mat[i][j])
                j-=1
            j+=1
            i-=1
            while i>ur:
                ans.append(mat[i][j])
                i-=1
            ur+=1
            lc+=1
            dr-=1
            rc-=1
        return ans
            
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends

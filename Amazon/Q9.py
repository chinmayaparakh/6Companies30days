#User function Template for python3

class Solution:
    def isValid(self, mat):
        # code here
        h=set()
        for i in range(9):
            for j in range(9):
                char=str(mat[i][j])
                if(int(char)!=0):
                    if ((i,(char)) in h) or ((char,j) in h) or ((char,i//3,j//3) in h):
                        return 0
               
                    h.add((i,(char)))
                    h.add(((char),j))
                    h.add(((char),i//3,j//3))
                       
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends

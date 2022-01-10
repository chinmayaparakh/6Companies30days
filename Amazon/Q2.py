class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        if n<3:
            return 0
        flag = True
        j=1
        c=0
        mx=0
        i=0
        
        while i < n-1:
            if flag==True:
                if arr[j]>arr[i]:
                    c+=1
                if arr[j]<arr[i] and c>=1:
                    flag=False
                    i-=1
                    j-=1
                if arr[i]==arr[j]:
                    c=0
                j+=1
                i+=1
                
            if flag==False:
                if arr[j]<arr[i]:
                    c+=1
                    j+=1
                    i+=1
                    if i-1==n-2 or arr[i]==arr[j]:
                        c+=1
                        mx=max(mx,c)
                        c=0
                        flag=True
                else:
                    c+=1
                    mx=max(mx,c)
                    c=0
                    flag=True
        return mx

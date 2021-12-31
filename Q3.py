def encode(arr):
    # Code here
    arr+=" "
    cnt=0
    out=""
    ele=arr[0]
    for i in arr:
        if i==ele:
            cnt+=1
        else:
            out+=ele+str(cnt)
            ele=i
            cnt=1
    return out
#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends

def nLargest(arr, n):
    arr.sort(reverse = True)
    for i in range(n):
        print (arr[i], end =" ") 

# Driver program
arr = [1, 10000, 123223, 455555569, 37657570, 287796666, 5268760]
n = int(input())
nLargest(arr, n)

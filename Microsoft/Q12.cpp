// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// User function template for C++

class Solution{
    public:
    // arr[] : int input array of integers
    // k : the quadruple sum required
    vector<vector<int> > fourSum(vector<int> &arr, int k) {
        // Your code goes here
        int n = arr.size();
        sort(arr.begin(), arr.end());
        set <vector<int>> s;
        for (int i=0; i<n; i++)
        {
            for (int j=i+1; j<n; j++)
            {
                int start = j+1;
                int end = n-1;
                while (start < end)
                {
                    long long sum = (long long )arr[i]+(long long )arr[j]+(long long )arr[start]+(long long)arr[end];
                    if (sum == k)
                    {
                        vector<int> temp = {arr[i], arr[j], arr[start], arr[end]};
                        s.insert(temp);
                        start++;
                        end--;
                    }
                    else if (sum > k)
                    {
                        end--;
                    }
                    else 
                    {
                        start++;
                    }
                }
            }
        }
            vector<vector<int>> ans (s.begin(), s.end());
            return ans;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k, i;
        cin >> n >> k;
        vector<int> a(n);
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        vector<vector<int> > ans = ob.fourSum(a, k);
        for (auto &v : ans) {
            for (int &u : v) {
                cout << u << " ";
            }
            cout << "$";
        }
        if (ans.empty()) {
            cout << -1;
        }
        cout << "\n";
    }
    return 0;
}  // } Driver Code Ends

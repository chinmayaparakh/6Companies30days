//TLE using Python therefore also used C++ on the same question

// { Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int maxProfit(int k, int n, int arr[]) {
        // code here
        int dp[k + 1][n];

        for(int i = 0; i <= k; i++) dp[i][0] = 0;
        for(int j = 0; j < n; j++) dp[0][j] = 0;
        
        for(int t = 1; t <= k; t++) {
        int mx = INT_MIN;
        for(int d = 1; d < n; d++) {
        
        mx = max(mx, dp[t - 1][d - 1] - arr[d - 1]);
        dp[t][d] = max(mx + arr[d], dp[t][d - 1]);
        }
        }
        
        return dp[k][n - 1];
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin >> K;
        cin >> N;
        int A[N];
        for (int i = 0; i < N; i++) cin >> A[i];

        Solution ob;
        cout << ob.maxProfit(K, N, A) << endl;
    }
    return 0;
}  // } Driver Code Ends

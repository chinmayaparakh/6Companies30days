// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution
{
    public:
    //Function to find unit area of the largest region of 1s.
    bool isValid(int r, int c, vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        if(r<0 || c<0 || r>=m || c>=n)
            return false;
        if(grid[r][c]==0)
            return false;
        return true;
    }
    
    int bfs(int i, int j, vector<vector<int>>& grid){
        
        queue<pair<int,int>> q;
        q.push({i,j});
        grid[i][j] = 0;
        int dx[] = {-1,0,1,1,1,0,-1,-1};
        int dy[] = {1,1,1,0,-1,-1,-1,0};
        int ans = 0;
        while(!q.empty()){
            pair<int,int> p = q.front();
            q.pop();
            int r = p.first;
            int c = p.second;
            ans++;
            for(int k=0; k<8; k++){
                if(isValid(r+dx[k], c+dy[k], grid)){
                    q.push({r+dx[k],c+dy[k]});
                    grid[r+dx[k]][c+dy[k]] = 0;
                }
            }
        }
        return ans;
    }
    int findMaxArea(vector<vector<int>>& grid) {
        // Code here
        int m = grid.size();
        int n = grid[0].size();
        int len = 0;
        int i,j;
        for(i=0; i<m; i++){
            for(j=0; j<n; j++){
                if( grid[i][j] == 1){
                    int curr = bfs(i,j,grid);
                    len = max(len,curr);
                }
            }
        }
        return len;
    }
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>grid(n, vector<int>(m, -1));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin >> grid[i][j];
			}
		}
		Solution obj;
		int ans = obj.findMaxArea(grid);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends

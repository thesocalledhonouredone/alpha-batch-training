#include <bits/stdc++.h>

using namespace std;

class Solution {
public:

    void dfs(int s, vector<vector<int>> &adj, vector<bool> &vis) {

        vis[s] = true;
        for(int i=0; i<adj.size(); i++) {
            if(adj[s][i] == 1 && vis[i] == 0) {
                dfs(i, adj, vis);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& adj) {

        int n = adj.size();
        vector<bool> vis(n, 0);
        int c = 0;

        for(int i = 0; i < n; i++) {
            if(vis[i] == 0) {
                dfs(i, adj, vis);
                c++;
            }
        }

        return c;
    }
};
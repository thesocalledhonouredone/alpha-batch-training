#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin>>t;
    while(t--){
        int n,m; cin>>n>>m;
        vector<vector<int>>adj(n+1);
        for(int i=0;i<m;i++){
            int u,v;cin>>u>>v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int s; cin>>s;
        vector<int> dist(n+1,-1);
        vector<bool> vis(n+1,0);
        queue<int> q;
        q.push(s);vis[s]=1;dist[s]=0;
        while(!q.empty()){
            int x=q.front();q.pop();
            for(int t:adj[x]){
                if(vis[t]==0){
                    vis[t]=1;q.push(t);dist[t]=dist[x]+6;
                }
            }
        }
        for(int i=1;i<=n;i++){
            if(i!=s)cout<<dist[i]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}

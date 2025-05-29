#include <bits/stdc++.h>
using namespace std;
int c;
void dfs(int s,vector<vector<int>>&adj,vector<bool>&vis){
    vis[s]=1;c++;
    for(int x:adj[s]){
        if(vis[x]==0)dfs(x,adj,vis);
    }
}
int main(){
    int n; cin>>n;
    vector<vector<int>>adj(2*n+1);
    for(int i=0;i<n;i++){
        int u,v; cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<bool> vis(2*n+1,0);
    int mx=0,mn=30000;
    for(int i=1;i<=n;i++){
        if(vis[i]==0){
            c=0;dfs(i,adj,vis);
            if(mx<c)mx=c;
            if(c>1 and mn>c)mn=c;
        }
    }
    cout<<mn<<" "<<mx;
}
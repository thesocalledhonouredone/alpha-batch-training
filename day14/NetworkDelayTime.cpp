#include<bits/stdc++.h>

using namespace std;

class Solution {

    typedef pair<int, int> p;

public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        
        vector<vector<p>> adj(n+1);
        for(auto x: times) {
            adj[x[0]].push_back({x[1], x[2]});
        }
        vector<int> dist (n+1, 1e9);
        dist[k] = 0;
        priority_queue<p, vector<p>, greater<p>> pq;
        pq.push({0, k});

        while(!pq.empty()) {
            auto [d, u] = pq.top();
            if(d > dist[u])
                continue;
            for(auto [v, w]: adj[u]) {
                if(dist[v] > d+w) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
        }

        int m = 0;
        for(int i = 1; i <= n; i++) {
            if(dist[i] == 1e9) {
                return -1;
            }
            m = max(m, dist[i]);
        }

        return m;
    }
};



// sir code: 
/* 

class Solution {
public:
    typedef pair<int,int> p;
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<p>> adj(n+1);
        for(auto x:times){adj[x[0]].push_back({x[1],x[2]});}
        vector<int> dist(n+1,1e9);
        dist[k]=0;
        priority_queue<p,vector<p>,greater<p>> pq;
        pq.push({0,k});
        while(!pq.empty()){
            auto [d,u]=pq.top();pq.pop();
            if(d>dist[u])continue;
            for(auto [v,w]:adj[u]){
                if(dist[v]>d+w){dist[v]=d+w;pq.push({dist[v],v});}
            }
        }
        int m=0;
        for(int i=1;i<=n;i++){
            if(dist[i]==1e9)return -1;
            m=max(m,dist[i]);
        }
        return m;
    }
};

*/
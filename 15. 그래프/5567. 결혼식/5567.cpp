#include <bits/stdc++.h>
using namespace std;

vector<int> adj[501];
int vis[501];

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin >> n >> m;
    for(int i = 1 ; i <= m ; i++){
        int u,v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }         

    for(int i = 1 ; i <= m ; i++){
        queue<int> q;
        q.push(i);
        
    }
}
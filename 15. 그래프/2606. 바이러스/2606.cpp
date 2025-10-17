#include <bits/stdc++.h>
using namespace std;

vector<int> adj[101];
bool vis[101];

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

    //BFS
    queue<int> q;
    q.push(1);
    vis[1] = true;
    int num = -1;
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        num++;
        for(auto nxt : adj[cur]){
            if(vis[nxt])
                continue;
            vis[nxt] = true;
            q.push(nxt);
        }
    }

    cout << num;

}
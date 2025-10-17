#include <bits/stdc++.h>
using namespace std;

vector<int> adj[1001]; //배열인데 vector를 원소로 가지는 배열이다.
bool vis[1001];

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
    int num = 0;
    for(int i = 1 ; i <= n ; i++){
        if(vis[i])
            continue;
        num++;
        queue<int> q;
        q.push(i);
        vis[i] = true;
        while(!q.empty()){
            int cur = q.front();
            q.pop();
            for(auto nxt : adj[cur]){
                if(vis[nxt])
                    continue;
                vis[nxt] = true;
                q.push(nxt);
            }
        }
    }
}
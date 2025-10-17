#include <bits/stdc++.h>
using namespace std;

vector<int> adj[1001];
bool vis[1001];
int n,m,st;

//재귀 dfs
void dfs(int cur){
    vis[cur] = true;
    cout << cur << ' ';
    for(auto nxt : adj[cur]){
        if(vis[nxt])
            continue;
        dfs(nxt);
    }
}

void bfs(){
    queue<int> q;
    q.push(st);
    vis[st] = true;
    while(!q.empty()){
        int cur = q.front();
        cout << cur << ' ';
        q.pop();
        for(auto nxt : adj[cur]){
            if(vis[nxt])
                continue;
            vis[nxt] = true;
            q.push(nxt);
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> st;
    for(int i = 1 ; i <= m ; i++){
        int u,v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    //작은거부터 방문하기 위해 정렬
    for(int i = 1 ; i <= n ; i++){
        sort(adj[i].begin(), adj[i].end());
    }

    dfs(st);
    fill(vis+1, vis+n+1, 0); //1 based index이기 때문에 조심!!
    cout << '\n';
    bfs();
}
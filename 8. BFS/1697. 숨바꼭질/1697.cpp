#include <iostream>
#include <queue>
using namespace std;
#define X first
#define Y second

int dist[100001];
int N,K;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> K;
    fill(dist, dist+100001, -1);
    dist[N] = 0;

    queue<int> Q;
    Q.push(N);

    while(dist[K] == -1){
        auto cur = Q.front();
        Q.pop();
        for(int nxt : {cur-1, cur+1, cur*2}){
            if(nxt < 0 || nxt > 100000)
                continue;   
            if(dist[nxt] >= 0)
                continue;
            dist[nxt] = dist[cur] + 1;
            Q.push(nxt);
        }
    }
    cout << dist[K];
}
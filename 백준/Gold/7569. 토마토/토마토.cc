#include <iostream>
#include <queue>
#include <tuple>
#include <utility>
using namespace std;

int board[101][101][101];
int dist[101][101][101];
int M,N,H;
int dx[6] = {1,0,-1,0,0,0};
int dy[6] = {0,1,0,-1,0,0};
int dz[6] = {0,0,0,0,1,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> M >> N >> H;
    queue<tuple<int,int,int>> Q;

    for(int i = 0 ; i < H ; i++){
        for(int j = 0 ; j < N ; j++){
            for(int k = 0 ; k < M ; k++){
                cin >> board[j][k][i];
                if(board[j][k][i] == 1)
                    Q.push({j,k,i});
                if(board[j][k][i] == 0)
                    dist[j][k][i] = -1;
            }
        }
    }

    while(!Q.empty()){
        auto cur = Q.front();
        Q.pop();
        for(int dir = 0 ; dir < 6 ; dir++){
            int nx = get<0>(cur) + dx[dir];
            int ny = get<1>(cur) + dy[dir];
            int nz = get<2>(cur) + dz[dir];
            if(nx < 0 || nx >= N || ny < 0 || ny >= M || nz < 0 || nz >= H)
                continue;
            if(dist[nx][ny][nz] >= 0)
                continue;
            dist[nx][ny][nz] = dist[get<0>(cur)][get<1>(cur)][get<2>(cur)] + 1;
            Q.push({nx,ny,nz});
        }
    }

    int ans = 0;
    for(int i = 0 ; i < H ; i++){
        for(int j = 0 ; j < N ; j++){
            for(int k = 0 ; k < M ; k++){
                if(dist[j][k][i] == -1){
                    cout << -1;
                    return 0;
                }
                ans = max(ans, dist[j][k][i]);
            }
        }
    }

    cout << ans;

}
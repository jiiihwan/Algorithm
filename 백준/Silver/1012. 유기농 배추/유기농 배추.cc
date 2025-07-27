#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

int board[51][51];
int vis[51][51];
int T,N,M,K;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> T;
    while(T--){
        cin >> M >> N >> K;

        for(int i = 0 ; i < M ; i++){
            fill(board[i], board[i]+M, 0);
            fill(vis[i], vis[i]+M, 0);
        }

        while(K--){
            int i,j;
            cin >> j >> i;
            board[i][j] = 1; //보드에 배추 위치에 1넣기
        }

        int ans = 0;
        for(int i = 0 ; i < N ; i++){ //다 돌아다니면서 bfs
            for(int j = 0 ; j < M ; j++){
                if(board[i][j] == 0 || vis[i][j] == 1)
                    continue;
                ans++;

                queue<pair<int,int>> Q;
                vis[i][j] = 1;                
                Q.push({i,j});


                while(!Q.empty()){
                    auto cur = Q.front();
                    Q.pop();
                    for(int dir = 0 ; dir < 4 ; dir++){
                        int nx = cur.X + dx[dir];
                        int ny = cur.Y + dy[dir];
                        if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                            continue;
                        if(board[nx][ny] == 0 || vis[nx][ny] == 1)
                            continue;
                        vis[nx][ny] = 1;
                        Q.push({nx,ny});
                    }
                     
                }


            }
        }

        cout << ans << '\n';

    }
}
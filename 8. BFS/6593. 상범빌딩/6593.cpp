#include <iostream>
#include <queue>
#include <tuple>
#include <utility>
using namespace std;

char board[31][31][31];
int dist[31][31][31];
int L, R, C;
int dx[6] = {1,0,-1,0,0,0};
int dy[6] = {0,1,0,-1,0,0};
int dz[6] = {0,0,0,0,1,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    while(1){
        cin >> L >> R >> C;
        if(L == 0 && R == 0 && C == 0)
            return 0;

        for(int i = 0 ; i < L ; i++){
            for(int j = 0 ; j < R ; j++){
                for(int k = 0 ; k < C ; k++){
                    dist[i][j][k] = -1; //dist -1로 초기화
                }
            }
        }

        queue<tuple<int,int,int>> Q;

        for(int i = 0 ; i < L ; i++){
            for(int j = 0 ; j < R ; j++){
                for(int k = 0 ; k < C ; k++){                    
                    cin >> board[i][j][k]; //입력받기

                    if(board[i][j][k] == 'S'){
                        Q.push({i,j,k}); //시작점 큐에 넣기
                        dist[i][j][k] = 0; //시작 거리는 0;
                    }
                }
            }
        }

        bool pass = false;
        while(!Q.empty()){ 
            if(pass)
                break;
            auto cur = Q.front();
            Q.pop();
            int curX, curY, curZ;
            tie(curX, curY, curZ) = cur;
            for(int dir = 0 ; dir < 6 ; dir++){
                int nx = curX + dx[dir];
                int ny = curY + dy[dir];
                int nz = curZ + dz[dir];
                if(nx < 0 || ny < 0 || nz < 0 || nx >= L || ny >= R || nz >= C)
                    continue;
                if(board[nx][ny][nz] == '#' || dist[nx][ny][nz] > 0) //벽이거나 방문했으면 pass
                    continue;
                if(board[nx][ny][nz] == 'E'){
                    cout << "Escaped in " << dist[curX][curY][curZ] + 1 << " minute(s).\n" ;
                    pass = true;
                    break;
                }
                dist[nx][ny][nz] = dist[curX][curY][curZ] + 1;
                Q.push({nx,ny,nz});
            }   
        }
        if(!pass)
            cout << "Trapped!\n";

    }

}
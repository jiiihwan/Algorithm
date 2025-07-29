#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

int board[301][301];
int dist[301][301];
int N,L;
int dx[8] = {1,2,2,1,-1,-2,-2,-1};
int dy[8] = {2,1,-1,-2,-2,-1,1,2};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    while(N--){
        cin >> L; //보드 길이 입력받기
        //보드 초기화
        for(int i = 0 ; i < L ; i++){ 
            fill(board[i], board[i]+L,0); //보드는 다 0으로
            fill(dist[i],dist[i]+L,-1); //dist는 다 -1로
        }
        int i,j,i2,j2;
        cin >> i >> j;
        dist[i][j] = 0; //나이트가 있는 곳은 거리가 0
        cin >> i2 >> j2;
        board[i2][j2] = 1; //도착해야할 곳은 1

        queue<pair<int,int>> Q;
        Q.push({i,j});

        while(!Q.empty()){
            auto cur = Q.front();
            Q.pop();
            for(int dir = 0 ; dir < 8 ; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 || nx >= L || ny < 0 || ny >= L)
                    continue;
                if(dist[nx][ny] >= dist[cur.X][cur.Y])
                    continue;
                if(board[cur.X][cur.Y] == 1){
                    cout << dist[cur.X][cur.Y] << '\n';
                    break;
                }
                if(board[nx][ny] == 1){
                    cout << dist[cur.X][cur.Y] + 1 << '\n';
                    while(!Q.empty()){
                        Q.pop();
                    }
                    break;
                } //dist
                dist[nx][ny] = dist[cur.X][cur.Y] + 1;
                Q.push({nx,ny});
            }
        }
    }
}
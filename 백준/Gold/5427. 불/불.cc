#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

string board[1001];
int fire[1001][1001];
int sg[1001][1001];
int N,w,h;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);



    cin >> N;
    while(N--){
        cin >> w >> h;
        for(int i = 0 ; i < h ; i++){
            cin >> board[i];
            fill(fire[i], fire[i]+w, -1);
            fill(sg[i], sg[i]+w, -1);
        }
        queue<pair<int,int>> Q1;
        queue<pair<int,int>> Q2;

        for(int i = 0 ; i < h ; i++){
            for(int j = 0 ; j < w ; j++){
                if(board[i][j] == '*'){
                    Q1.push({i,j});
                    fire[i][j] = 0;
                }
                if(board[i][j] == '@'){
                    Q2.push({i,j});
                    sg[i][j] = 0;
                }       
            }
        }

        //불 먼저 bfs
        while(!Q1.empty()){
            auto cur = Q1.front();
            Q1.pop();
            for(int dir = 0 ; dir < 4 ; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 || nx >= h || ny < 0 || ny >= w)
                    continue;
                if(board[nx][ny] == '#' || fire[nx][ny] >= 0)
                    continue;
                fire[nx][ny] = fire[cur.X][cur.Y] + 1;
                Q1.push({nx,ny});
            }
        }

        //상근이 bfs
        bool success = false;
        while(!Q2.empty()){
            auto cur = Q2.front();
            Q2.pop();
            for(int dir = 0 ; dir < 4 ; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 || nx >= h || ny < 0 || ny >= w){
                    cout << sg[cur.X][cur.Y] + 1 << '\n';
                    success = true;
                    while(!Q2.empty()) Q2.pop();
                    break;
                }
                if(board[nx][ny] == '#' || sg[nx][ny] >= 0) //벽이거나 이미 간곳
                    continue;
                if(sg[cur.X][cur.Y] + 1 >= fire[nx][ny] && fire[nx][ny] != -1) //상근이보다 불이 빠른경우
                    continue;
                sg[nx][ny] = sg[cur.X][cur.Y] + 1;
                Q2.push({nx,ny});
            }
        }

        if(!success)
            cout << "IMPOSSIBLE" << '\n';

    }
}
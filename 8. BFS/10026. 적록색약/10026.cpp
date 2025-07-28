#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

string board[101];
int vis[101][101];
int vis2[101][101];
int N;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    for(int i = 0 ; i < N ; i++){
        cin >> board[i]; //board초기화
    }

    int normal=0;
    char color;
    for(int i = 0 ; i < N ; i++){ //모든 board의 원소 다 돌면서 bfs
        for(int j = 0 ; j < N ; j++){
            if(vis[i][j]) //방문한곳은 안간다
                continue;

            normal++;    
            if(board[i][j] == 'R')
                color = 'R';
            else if(board[i][j] == 'G')
                color = 'G';
            else
                color = 'B';

            queue<pair<int,int>> Q;
            vis[i][j] = 1;
            Q.push({i,j});

            while(!Q.empty()){
                auto cur = Q.front();
                Q.pop();
                for(int dir = 0 ; dir < 4 ; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= N || ny < 0 || ny >= N)
                        continue;
                    if(board[nx][ny] != color || vis[nx][ny])
                        continue;
                    vis[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
        }
    }

    for(int i = 0 ; i < N ; i++){ //모든 board의 원소 다 돌면서 bfs
        for(int j = 0 ; j < N ; j++){  
            if(board[i][j] == 'G')
                board[i][j] = 'R';
        }
    }

    int not_normal=0;
    for(int i = 0 ; i < N ; i++){ //모든 board의 원소 다 돌면서 bfs
        for(int j = 0 ; j < N ; j++){  
            if(board[i][j] == 'R')
                color = 'R';
            else
                color = 'B';

            if(vis2[i][j]) //방문한곳은 안간다
                continue;
            not_normal++;  

            queue<pair<int,int>> Q;
            vis2[i][j] = 1;
            Q.push({i,j});

            while(!Q.empty()){
                auto cur = Q.front();
                Q.pop();
                for(int dir = 0 ; dir < 4 ; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= N || ny < 0 || ny >= N)
                        continue;
                    if(board[nx][ny] != color || vis2[nx][ny])
                        continue;
                    vis2[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
        }
    }    


    cout << normal << ' ' << not_normal;
}
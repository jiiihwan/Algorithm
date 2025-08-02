#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

int board[101][101];
int height[101][101];
int N;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    int max_height = 0;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
            max_height = max(max_height, board[i][j]);
        }
    }


    //int suwi = 0;
    int ans = 0;
    //int board_size = N^2;

    for(int suwi = 0 ; suwi <= max_height ; suwi++){
        int count = 0;
        for(int i = 0 ; i < N ; i++)
            fill(height[i], height[i] + N, 0);
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < N ; j++){
                if(board[i][j] <= suwi || height[i][j] > 0) //현재 수위이하면 패스
                    continue;
                count++;
                queue<pair<int,int>> Q;
                Q.push({i,j});
                height[i][j] = 1; //방문처리

                while(!Q.empty()){
                    auto cur = Q.front();
                    Q.pop();
                    for(int dir = 0 ; dir < 4 ; dir++){
                        int nx = cur.X + dx[dir];
                        int ny = cur.Y + dy[dir];
                        if(nx < 0 || nx >= N || ny < 0 || ny >= N)
                            continue;
                        if(board[nx][ny] <= suwi || height[nx][ny] > 0) //현재 수위이하면 패스 or 이미 수위를 쟀으면 패스
                            continue;
                        height[nx][ny] = 1;
                        Q.push({nx,ny});
                    }
                }
                
            }
        }
        ans = max(ans, count); //ans랑 count중에 큰걸 저장
    }

    cout << ans;

}
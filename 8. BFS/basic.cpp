#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

int board[502][502];
bool vis[502][502]; //visit
int n = 7, m = 10;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    queue<pair<int,int>> Q;
    vis[0][0] = 1;
    Q.push({0,0});

    while(!Q.empty()){
        pair<int,int> cur = Q.front();
        Q.pop();
        //cout << '(' << cur.X << ", " << cur.Y << ") ->";

        //여기부턴 진짜 외우기
        for(int dir = 0; dir < 4; dir++){
            int nx = cur.X + dx[dir]; //아래거부터 시계방향으로 돌면서 조회
            int ny = cur.Y + dy[dir]; 
            if(nx < 0 || nx >= n || ny < 0 || ny >=m) //보드 범위 벗어난 경우 다음칸
                continue;
            if(vis[nx][ny] || board[nx][ny] != 1) //조회할 칸이 아닌 경우 다음칸
                continue;
            vis[nx][ny] = 1; //방문 표시 남기기
            Q.push({nx,ny});
        }
    }
}

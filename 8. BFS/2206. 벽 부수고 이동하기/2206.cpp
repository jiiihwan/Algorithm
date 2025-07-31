#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

string board[1001];
int dist[1001][1001];
int dist2[1001][1001];
int N,M;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
bool pass = false;
pair<int,int> breaked_wall;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < N ; i++)
        cin >> board[i];
    
    dist[N-1][M-1] = -1;

    queue<pair<int,int>> Q;
    queue<pair<int,int>> Q2;
    Q.push({0,0});
    dist[0][0] = 1;

    while(!Q.empty()){
        auto cur = Q.front();
        Q.pop();
        for(int dir = 0 ; dir < 4 ; dir++){
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                continue;
            if(board[nx][ny] == '1'){
                dist2[nx][ny] = min(dist2[cur.X][cur.Y] + 1, dist2[nx][ny]); //dist2 에 벽 시간 기록
                Q2.push({nx,ny});
                continue;
            } //벽을 만나면
            if(dist[nx][ny] > 0) //이미 지나온 길이면
                continue;
            dist[nx][ny] = dist[cur.X][cur.Y] + 1;
            Q.push({nx,ny});
            breaked_wall = cur;
        }
    }
    //통과했다면
    if(dist[N-1][M-1] != -1){
        pass = true; //벽에 안막혔다는 뜻
        breaked_wall = {0,0}; //부술 벽 초기화
    }
    //통과했으면 breaked_wall 찾아야하는데 이건 일단
    // 1. 모든벽에 bfs돌리고
    // 2. 벽 뚫은 순간부터 n,m 에 도착할때까지의 시간을 min변수에 기록
    // 3. 그때의 벽 좌표를 저장
    //통과못했으면 breakd_wall 이 부술벽이고 이거 board에서 0으로 바꾸고 bfs돌리면됨
    //

    if(pass){
        while(!Q2.empty()){
            //int dist3[1001][1001];
            /*
            for(int i = 0 ; i < N ; i++){
                for(int j = 0 ; j < M ; j++){
                    dist3[i][j] = 0;
                }
            }
            */
            auto cur = Q2.front();
            Q2.pop();
            for(int dir = 0 ; dir < 4 ; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                    continue;
                if(board[nx][ny] == '1'){
                    continue;
                } //벽을 만나면
                if(dist2[nx][ny] > 0){ 
                    dist2[nx][ny] = min(dist2[cur.X][cur.Y] + 1, dist2[nx][ny]);
                    continue;
                }//이미 값이 있을때 더 작은걸 넣는다
                dist2[nx][ny] = dist2[cur.X][cur.Y] + 1;
                Q2.push({nx,ny});
            }
        }
    }
    else{
        board[breaked_wall.X][breaked_wall.Y] = 0;

        while(!Q.empty()){
            auto cur = Q.front();
            Q.pop();
            for(int dir = 0 ; dir < 4 ; dir++){
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                    continue;
                if(board[nx][ny] == '1' || dist[nx][ny] > 0)
                    continue;
                dist[nx][ny] = dist[cur.X][cur.Y] + 1;
                Q.push({nx,ny});
            }
        }
    }

    
    cout << dist[N-1][M-1];

}
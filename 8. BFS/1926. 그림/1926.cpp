#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

int board[502][502];
bool vis[502][502];
int n, m;
int dx[4] = {1,0,-1,0}; //하 우 상 좌
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++)
            cin >> board[i][j]; //board에 주어진 값 채워넣기
    
    int mx = 0; //그림의 최댓값
    int num = 0; //그림의 수

    //모든 칸 조회
    for(int i = 0 ; i < n ; i++){ 
        for(int j = 0 ; j < m ; j++){
            if(board[i][j] == 0 || vis[i][j]) //만약 필요없는 곳이거나 방문했다면 다음으로 넘어감(continue)
                continue;
            num++; //처음만나는 그림이니 카운팅
            
            queue<pair<int, int>> Q;
            vis[i][j] = 1; // 방문 표시
            Q.push({i,j}); //방문한거 큐에 담기
            
            int area = 0;
            while(!Q.empty()){
                area++; //탐색하면서 넓이 재기

                pair<int,int> cur = Q.front(); //현재 검사하는 곳은 큐의 front
                Q.pop(); //검사하는건 큐에서 빼기

                //지금 칸의 시계방향 돌면서 4칸 방문
                for(int dir = 0 ; dir < 4 ; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= n || ny < 0 || ny >= m)  //범위를 벗어난 경우
                        continue;
                    if(vis[nx][ny] || board[nx][ny] != 1) //방문했거나 1이 아닌경우
                        continue;
                    vis[nx][ny] = 1; //방문표시
                    Q.push({nx,ny}); 
                }
            }

            mx = max(mx, area); //mx에 최댓값 저장

        }
    }
    cout << num << '\n' << mx;
}

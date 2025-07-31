#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;
#define X first
#define Y second

int board[101][101];
int vis[101][101];
int N,M,K;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> M >> N >> K;

    while(K--){
        int i1,j1,i2,j2;
        cin >> i1 >> j1 >> i2 >> j2;
        i2--;
        j2--;
        //board에 사각형있는곳은 1넣기
        for(int i = i1 ; i <= i2 ; i++){
            for(int j = j1 ; j <= j2 ; j++){
                board[i][j] = 1;
                vis[i][j] = 1;
            }
        }
    }
    vector<int> ans;

    //모든 칸을 돌면서 bfs
    //while문 도는 횟수가 영역의 개수
    int count = 0;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            queue<pair<int,int>> Q;
            //방문안한곳 방문
            if(vis[i][j] == 0){ //여기에 continue가 있어야한다.
                Q.push({i,j});
                vis[i][j] = 1;
                count++;
            }

            int area = 0; 
            while(!Q.empty()){
                area++;
                auto cur = Q.front();
                Q.pop();
                for(int dir = 0 ; dir < 4 ; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                        continue;
                    if(board[nx][ny] || vis[nx][ny])
                        continue;
                    vis[nx][ny] = 1;
                    Q.push({nx,ny});
                }
            }
            if(area != 0)
                ans.push_back(area);
            
        }
    }

    cout << count << '\n';

    sort(ans.begin(),ans.end());

    for(int i : ans)
        cout << i << ' ';
        
}
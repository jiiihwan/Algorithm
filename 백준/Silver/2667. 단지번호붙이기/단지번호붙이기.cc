#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;
#define X first
#define Y second

string board[26];
int vis[26][26];
int N, danji = 1;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for(int i = 0 ; i < N ; i++)
        cin >> board[i];
    

    vector<int> ans;

    int count = 0;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(board[i][j] == '0' || vis[i][j] > 0 ) //건물이 없거나 단지가 표시된 곳은 패스
                continue;
            count++;
            
            queue<pair<int,int>> Q;
            Q.push({i,j});
            vis[i][j] = count;

            int area = 0;
            while(!Q.empty()){
                area++;
                auto cur = Q.front();
                Q.pop();
                for(int dir = 0 ; dir < 4 ; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];
                    if(nx < 0 || nx >= N || ny < 0 || ny >= N)
                        continue;
                    if(board[nx][ny] == '0' || vis[nx][ny] > 0 ) //건물이 없거나 단지를 적은곳은 패스
                        continue;
                    vis[nx][ny] = count;
                    Q.push({nx,ny}); 
                }
            }
            ans.push_back(area);
            //danji++;
        }
    }

    sort(ans.begin(), ans.end()); //오름차순 정렬

    cout << count << '\n';
    for(int i : ans){
        cout << i << '\n';
    }
}
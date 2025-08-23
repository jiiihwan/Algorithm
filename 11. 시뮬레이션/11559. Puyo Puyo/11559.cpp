#include <iostream>
#include <utility>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
#define X first
#define Y second

char board[12][6];
int vis[12][6];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int boom = 0;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    for(int i = 0 ; i < 12 ; i++){
        for(int j = 0 ; j < 6 ; j++){
            cin >> board[i][j];
        }
    }

    while(1){
        //vis 배열 초기화
        for(int i = 0 ; i < 12 ; i++)
            fill(vis[i], vis[i]+6, 0);
        
        queue<pair<int,int>> Q;
        vector<pair<int,int>> temp; //bfs돌면서  담기
        vector<pair<int,int>> del; //제거할거 담기
        for(int i = 0 ; i < 12 ; i++){
            for(int j = 0 ; j < 6 ; j++){
                if(board[i][j] == '.' || vis[i][j] == 1)
                    continue;
                Q.push({i,j});
                temp.push_back({i,j}); //현재꺼 일단담기
                vis[i][j] = 1;

                int count = 0;
                while(!Q.empty()){
                    count++;
                    auto cur = Q.front();
                    Q.pop();
                    for(int dir = 0 ; dir < 4 ; dir++){
                        int nx = cur.X + dx[dir];
                        int ny = cur.Y + dy[dir];
                        if(nx < 0 || nx >= 12 || ny < 0 || ny >= 6)
                            continue;
                        if(vis[nx][ny]) //방문했으면 패스
                            continue;
                        if(board[cur.X][cur.Y] != board[nx][ny]) //현재꺼랑 다르면 패스
                            continue;
                        vis[nx][ny] = 1;
                        Q.push({nx,ny});
                        temp.push_back({nx,ny});
                    }
                }
                //만약 bfs돌았는데 4개 이하라면 del에 저장된거 다 지우기
                if(count >= 4){
                    for(auto t : temp)
                        del.push_back(t);
                }
                temp.clear();
                
            }
        }

        // 수정된 중력 적용 로직
        if(!del.empty()){
            boom++;
            // 1. 터진 뿌요들을 모두 '.'으로 변경
            for(auto d : del){
                board[d.X][d.Y] = '.';
            }

            // 2. 스왑(swap) 방식으로 중력 적용
            for(int j = 0; j < 6; j++){ // 각 열에 대해
                for(int i = 10; i >= 0; i--){ // 아래에서부터 위로 올라가며
                    int current_row = i;
                    // 현재 칸에 뿌요가 있고, 그 아래 칸이 비어있다면 계속 내림
                    while(current_row < 11 && board[current_row+1][j] == '.'){
                        swap(board[current_row][j], board[current_row+1][j]);
                        current_row++;
                    }
                }
            }
        }
        else {
            cout << boom;
            return 0;
        }
        del.clear();
    }

}

/*
떨어지는 거 구현
1. bfs 돌면서 카운트하고 4개 이상이면 지워야할 좌표 저장, 이후에 완탐 하면서 지워야할 좌표의 열좌표는 
가만히 두고 행좌표에 있는것들을 한칸씩 내린다
2. 그리고 boom++
4. vis배열 초기화 하고 다시 bfs 시작
*/
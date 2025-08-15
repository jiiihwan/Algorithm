#include <iostream>
#include <queue>
#include <utility>
using namespace std;
#define X first
#define Y second

int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0}; //동남서북
int N,M;
int room[8][8];
vector<pair<int,int>> pos; //cctv가 있는 좌표를 담는 곳
int ans = 64;

void check(int x, int y, int dir){
    dir %= 4; 
    while(1){
        x += dx[dir];
        y += dy[dir];
        if(x < 0 || x >= N || y < 0 || y >= M) //범위를 벗어나면 종료
            return;
        if(room[x][y] == 6) //벽을 만나면 종료
            return;
        if(room[x][y] != 0) //이미 기록되어있는 칸이면 패스
            continue;
        room[x][y] = 7; //0이면 room에다가 7넣기
    }
}

//idx 번째 cctv 를 회전
void solve(int idx){
    int cnt = pos.size(); //cnt = cctv의 개수
    if(idx == cnt){ //base condition - 개수만큼 다 돌면 카운트 시작
        int tmp = 0;
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M ; j++){
                if(room[i][j] == 0)
                    tmp++; //room을 순회하면서 사각지대의 개수를 카운트한다
            }
        }
        ans = min(tmp,ans);
        return;
    }

    int x = pos[idx].X;
    int y = pos[idx].Y; //0번째 cctv부터 시작
    int backup[8][8];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            backup[i][j] = room[i][j]; //backup에 room 복사해서 초기화
        }
    }

    for(int dir = 0 ; dir < 4 ; dir++){ //4방향 다 돌기
        if(room[x][y] == 1){
            check(x,y,dir);
        }
        else if(room[x][y] == 2){
            check(x, y, dir); //dir == 0 일때 right
            check(x, y, dir + 2); //dir == 0 일때 left
        }
        else if(room[x][y] == 3){
            check(x, y, dir); //dir == 0 일때 right
            check(x, y, dir + 1); //dir == 0 일때 up
        }
        else if(room[x][y] == 4){
            check(x, y, dir); //dir == 0 일때 right
            check(x, y, dir + 1); //dir == 0 일때 up
            check(x, y, dir + 2); //dir == 0 일때 left
        }
        else if(room[x][y] == 5){
            check(x, y, dir); //dir == 0 일때 right
            check(x, y, dir + 1); //dir == 0 일때 up
            check(x, y, dir + 2); //dir == 0 일때 left
            check(x, y, dir + 3); //dir == 0 일때 down
        }
        solve(idx + 1); //다음 cctv 회전시키기
        for (int i = 0; i < N; i++) { //다음 cctv 회전이 끝나고 돌아오면 원래 백업으로 돌아온다
            for (int j = 0; j < M; j++) {
                room[i][j] = backup[i][j];
            }
        }
    }

}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> room[i][j];
            if (room[i][j] >= 1 && room[i][j] <= 5) {
                pos.push_back({i,j}); //cctv가 있는 좌표를 담기
            }
        }
    }
    solve(0);
    cout << ans;
}
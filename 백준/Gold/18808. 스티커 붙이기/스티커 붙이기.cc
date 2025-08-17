#include <iostream>
#include <utility>
#include <vector>
#include <queue>
using namespace std;
#define X first
#define Y second

int n,m,k,r,c;
int board[41][41];
int sticker[11][11];
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0}; //동남서북
queue<pair<int,int>> pos; //붙힐 좌표 저장

bool attachable(int x, int y){
    if(r > n || c > m) 
        return false;
    //스티커 순회하면서 보드랑 비교, 붙을 수 있는지 판단 - 스티커가 존재하는 영역에 보드에 뭐가 붙어져있으면 못 붙음
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            if(sticker[i][j] && board[x+i][y+j] == 1)
                return false;
        }
    }
    return true;
}

bool attach_sticker(){
    bool ok=false;
    for(int i = 0 ; i <= n-r ; i++){
        if(ok)
            break;
        for(int j = 0 ; j <= m-c ; j++){
            if(!attachable(i,j))
                continue;
            else{
                pos.push({i,j});
                ok = true;
                break;
            } //붙히는 게 가능하다면 붙힐 좌표 저장
        }
    }
    if(pos.empty()) //붙히는 게 불가능하면 안붙히고 버림
        return false;
    //노트북의 붙힐수 있는 좌표부터 스티커가 존재하는 곳 그대로 복사
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            if(sticker[i][j])
                board[pos.front().X + i][pos.front().Y + j] = 1;
        }
    }
    pos.pop();
    return true;
}

void spin(){
    //대각으로 뒤집기
    int temp[11][11];
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            temp[j][r - 1 - i] = sticker[i][j];
    swap(r,c); //r c 가 각각 행 열 에 대응되도록 바꿔주기
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            sticker[i][j] = temp[i][j];
}

void ans_count(){
    //board를 돌아다니며 1 개수 세고 출력
    int ans = 0;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            if(board[i][j] == 1)
                ans++;
        }
    } 
    cout << ans ;
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m >> k;
    while(k--){
        cin >> r >> c;
        for(int i = 0 ; i < r ; i++){
            for(int j = 0 ; j < c ; j++){
                cin >> sticker[i][j]; //현재 들어온 스티커 입력
            }
        } 

        //스티커 붙히기 실패하면 spin 하고 성공하면 break
        for(int i = 0 ; i < 4 ; i++){
            if(!attach_sticker())
                spin();
            else
                break;
        }

    }

    ans_count();
}
#include <iostream>
using namespace std;

int N;
char board[64][64];

bool check(int x, int y, int n){
    for(int i = x ; i < x+n ; i++){
        for(int j = y ; j < y+n ; j++){
            if(board[x][y] != board[i][j])
                return false;
        }
    }
    return true;
}

void solve(int x, int y, int n){
    if(check(x,y,n)){ //네모 안이 다 같은 경우
        cout << board[x][y];
        return;
    }
    cout << '(';
    //네모 안이 다른 경우
    for(int i = 0 ; i < 2 ; i++){
        for(int j = 0 ; j < 2 ; j++){
            solve(x+i*n/2, y+j*n/2, n/2);
        }
    }
    cout << ')';
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> board[i][j];
        }
    }

    solve(0,0,N);
}
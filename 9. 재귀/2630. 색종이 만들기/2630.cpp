#include <iostream>
using namespace std;

int N;
int paper[128][128];
int color[2];

bool check(int x, int y, int n){
    for(int i = x ; i < x + n ; i++){
        for(int j = y ; j < y + n ; j++){
            if(paper[x][y] != paper[i][j])
                return false; 
        }
    }
    return true;
}

void solve(int x, int y, int n){
    if(check(x,y,n)){
        color[paper[x][y]]++; //paper에 있는 색깔 개수가 ++
        return;
    }
    for(int i = 0 ; i < 2 ; i++){
        for(int j = 0 ; j < 2 ; j++){
            solve(x + i*n/2, y + j*n/2, n/2);
        }
    }

}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> paper[i][j];
        }
    }

    solve(0,0,N);

    for(int i : color)
        cout << i << '\n';
}
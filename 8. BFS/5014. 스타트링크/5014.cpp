#include <iostream>
#include <queue>
using namespace std;

int board[1000001];
int F,S,G,U,D;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> F >> S >> G >> U >> D;
    fill(board, board+1000001, -1);
    board[S] = 0;

    queue<int> Q;
    Q.push(S);
    while(board[G] == -1){
        if(Q.empty()){
            cout << "use the stairs";
            return 0;
        }
        auto cur = Q.front();
        Q.pop();
        for(int i : {U,-D}){
            int nxt = cur + i;
            if(nxt < 1 || nxt > F)
                continue;
            if(board[nxt] >= 0)
                continue;
            board[nxt] = board[cur] + 1;
            Q.push(nxt);
        }
    }

    cout << board[G];

}
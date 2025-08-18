#include <iostream>
#include <utility>
#include <queue>
using namespace std;

int n,ans=0;
int board[21][21];

void move_left(){
    queue<int> q;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            if(board[i][j] > 0){
                q.push(board[i][j]);
            } 
        } 
    }
    for(int i = 0 ; i < n ; i++){
        while(!q.empty()){
            int j = 0;
            if(board[i][j] == q.front()){
                board[i][j] = 2 * q.front();
                j--;
            }
            else{
                board[i][j] = q.front();
            }
            q.pop();
            j++;
        }
    }

}


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < n ; j++)
            cin >> board[i][j];
    
    move_left();
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            cout << board[i][j] << ' ';
        }
        cout << '\n';
    }

}
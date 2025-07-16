#include <iostream>
#include <queue>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N,ans;
    queue<int> Q;

    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        Q.push(i);
    }


    for(int i = 0 ; Q.size() > 1 ; i++){
        if((i & 1) == 0){ //짝수
            Q.pop();
        }
        else{
            Q.push(Q.front());
            Q.pop();
        }
    }

    cout << Q.front();
}
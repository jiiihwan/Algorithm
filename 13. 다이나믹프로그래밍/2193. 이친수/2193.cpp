#include <bits/stdc++.h>
using namespace std;

long long D[91][2]; //이친수의 개수가 담겨있는 문자열, [0]은 0으로 끝나는 경우, [1]은 1로 끝나는 경우

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    
    D[1][0] = 0;
    D[1][1] = 1;
    D[2][0] = 1;
    D[2][1] = 0;

    for(int i = 3 ; i <= n ; i++){
        D[i][0] = D[i-1][0] + D[i-1][1];
        D[i][1] = D[i-1][0]; 
    }

    cout << D[n][0] + D[n][1];
}
#include <bits/stdc++.h>
using namespace std;

long long D[101][10]; //

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    int MOD = 1000000000;
    cin >> N;

    for(int i = 1 ; i <= 9 ; i++)
        D[1][i] = 1;

    for(int i = 2 ; i <= N ; i++){
        D[i][0] = D[i-1][1] % MOD;
        D[i][9] = D[i-1][8] % MOD;
        for(int j = 1 ; j <= 8 ; j++){
            D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % MOD; 
        }
    }

    long long ans = 0;
    for(int i = 0 ; i <= 9 ; i++){
        ans += D[N][i];
    }

    cout << ans % MOD;
}